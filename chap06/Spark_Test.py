#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()

import pyspark              # only run after findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()

