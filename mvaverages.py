#!/usr/bin/env python
# coding: utf-8


import findspark
findspark.init('c:/Spark')



# *******************Importing different Libraries**********************
import pyspark
import sys
import boto3
import pandas as pd



#*******************Moving Average function**********************

def moving_av(n, window_size):
    t_series = pd.Series(n)
    windows = t_series.rolling(window_size)
    moving_averages = windows.mean()   
    return (moving_averages[-1:])





