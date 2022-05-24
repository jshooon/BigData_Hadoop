#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from hdfs import InsecureClient

client_hdfs = InsecureClient('http://192.168.43.128:9870')  # namenode의 웹 인터페이스
with client_hdfs.read('/user/mydata/mydata.csv') as reader:
    df = pd.read_csv(reader,index_col=0)
print( df )

