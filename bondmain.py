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
from element_call import *
import logging



logger = logging.getLogger(__name__)

def main():
    
    #*****************req 1. Moving Averages of a list************* 
    
        #initializing the starting list
    n = [1, 2, 3, 7, 9]
    
        #aquiring the window size for moving averages as not stated in the challenge
    window_size = int(input("Enter moving average window size: "))

   
    x = moving_av(n, window_size)
    print (x)
   
    #*****************req 2. Adding element to the list*************

    
    
    y = add_elements(n)
    print(y)
    
    #*****************req 3. accessing a certain element from the list WITH error handling*************  
    
    p = element_call(y)
    print(p)
    


if __name__ == "__main__":
    main()




