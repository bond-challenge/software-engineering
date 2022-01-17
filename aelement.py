#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import findspark
findspark.init('c:/Spark')

# from pyspark import SparkContext


# In[ ]:


# *******************Importing different Libraries**********************
import pyspark
import sys
import boto3
import pandas as pd


# In[ ]:


#********************Add elements func***************************
def add_elements (n):
    val = int(input("input element to be added:"))
    n.append(val)
    return n
    

