#!/usr/bin/env python
'''
  Process moving elements stream
'''

import argparse
from Queue import Queue
import re
import subprocess
import threading
import time
import yaml

class EventConsumer(object):
    ''' Submits events to desired file or app '''

    def __init__(self, args, queue):
        self.queue = queue
        self.args = args

    def run(self):
        ''' main function '''

        while True:
            event_list = []
            while not self.queue.empty():
                event = self.queue.get()
                if self.args.debug:
                    print "Processing event: {}".format(str(event))
                event_list.append(event)

            # initialize event counts so that we send '0' events
            # in the case where no events were received
            event_counts = {}

            # add up each distinct event
            for event in event_list:
                event_counts[event] += 1

            if self.args.verbose or self.args.dry_run:
                print "Got events: " + str(event_counts)

            if not self.args.dry_run:
                for event, count in event_counts.iteritems():
                    print "Got events: " + str(event)
                return str(event)

            time.sleep(self.args.reporting_period)

        # Never should get here

class EventWatcher(object):
    ''' Watches event stream '''

    def __init__(self, queue):
        self.args = None
        self.queue = queue
        self.parse_args()

    def run(self):
        '''  Main function '''

        self.event_watch_loop()

    def parse_args(self):
        ''' parse the args from the cli '''

        parser = argparse.ArgumentParser(description='Event watcher')
        parser.add_argument('-v', '--verbose', action='store_true',
                            default=None, help='Verbose?')
        parser.add_argument('--debug', action='store_true',
                            default=None, help='Debug?')
        parser.add_argument('--dry-run', action='store_true', default=False,
                            help='Do not send results to the target file or app')
        parser.add_argument('--reporting-period', default=60, type=int,
                            help='How many seconds between each reporting period')

        self.args = parser.parse_args()


    def event_watch_loop(self):
        ''' Loop to read/process incoming events '''

        while True:
            # here I just took a file to which is streaming n elements every few seconds and process these events in
            # a local environment but same can be done in Azure to use EVent Grid automatically trigger this script which can be deployed as
            # the azure function app
            # in real case sceanrios it could be Azure Event hub or Event Grid as input for streaming data
            # which can be also configured given the details of connection strings and client secrets.
            popen = subprocess.Popen(['tail', 'Get-Content', 'test.csv', '-Wait', '-Tail', '50'], bufsize=1,
                                     stdout=subprocess.PIPE)

            for line in iter(popen.stdout.readline, b''):
                    if self.args.debug:
                        print line

                    result = line
                    if result:
                        if self.args.verbose:
                            print line
                        self.queue.put(result)

            # Never should get here - but if it does, add a cool-off timer for a minute or desired time
            # to avoid smashing repeated streaming events or calls.
            time.sleep(self.args.reporting_period)

if __name__ == '__main__':
    event_queue = Queue()

    OEW = EventWatcher(event_queue)
    watch_thread = threading.Thread(target=OEW.run)
    watch_thread.start()

    OEC = EventConsumer(OEW.args, event_queue)
    event_consumer = threading.Thread(target=OEC.run)
    event_consumer.start()
