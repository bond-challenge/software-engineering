"""
Title: Moving Average
Author: Marcus Eberhardt
Status: Active
Type: Assessment Bond Loyality
Created On: 02-06-2021
Last Modified By:
Last Modified On:
Description:
Modifications:

"""

# [START imports]
from datetime import datetime, timedelta
import os
import numpy as np
import io
import time
import os,sys,inspect
import argparse

#parser = argparse.ArgumentParser()
#parser.add_argument('-a', '--arg', nargs='+', type=int)

#print parser.parse_args()
#value = parser.parse_args()
#print(value.list)

p = argparse.ArgumentParser()

# accept two lists of arguments
# like -a 1 2 3 4 -b 1 2 3
p.add_argument('-a', nargs="+", type=int)
p.add_argument('-b', nargs="+", type=int)
args = p.parse_args()

x = set(args.a)
set_b = set(args.b)

#print(set_a)

#def get_args():
#    args = getattr(get_args, '_args', None)
#    if args is None:
        # default message can be overridden with the usage= keyword argument
        #parser = argparse.ArgumentParser(prog='MovingAverage', #overwrite name of program at runtime
        #                                 usage='%(prog)s [options]', #application usage statement
        #                                 allow_abbrev=True, #allow abbreviated arg names
        #                                 add_help=True, #enable program help (i.e. --h | --help)
        #                                 description='getting list of latest N records for moving average.')

#        parser.add_argument('--array',

#                            action='store',
#                            help='<Required> submit list',
#                            required=True)

#        args = get_args._args = parser.parse_args()
#    return args



#x = np.array([5,3,8,10,2,1,5,1,0,2])
#x = value.list
y = 2
x = int(x)
def get_moving_average(x,y):
    """
    calculate the moving average from input list
    """
    try:
        return np.convolve(x, np.ones(y), 'valid') / y
        print(np)
    except Exception as e:
        #error.report_error(e)
        print('F')
        #log_error(e)
        raise


if __name__ == "__main__":
    try:
        executionStartTimer = time.perf_counter()
        execution_start_time = datetime.utcnow()
        #get_args()
        print(get_moving_average(x, y))

        print('success')
    except Exception as e:
        error_message = f'An exception occurred: {e}'
        print(error_message)
        #error.report_error(e)
        #log_status("Execution of Job Get Moving Average, started:", execution_start_time, 0, "FAILED", executionStartTimer)
        #log_error(e)
