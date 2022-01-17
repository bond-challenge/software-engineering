#!/usr/bin/env python
# coding: utf-8


import findspark
findspark.init('c:/Spark')


# *******************Importing different Libraries**********************
import pyspark
import sys
import boto3
import pandas as pd
from mvaverages import *
from aelement import *
import logging






def element_call(y):
    logger = logging.getLogger(__name__)
    try:
        el= int(input("give the element number you want: "))
        if len(y) > el or len(y) == el:
            return(y[el-1])
        else:
            print ("Invalid element as input")
    except Exception as error :
        logger.info("error msg", error )
       

