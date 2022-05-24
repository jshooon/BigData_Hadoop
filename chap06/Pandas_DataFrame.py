#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.DataFrame({'A':[2,4,8],
              'B':[5,8,2],
              'C':[9,5,7]})


# In[5]:


df


# In[6]:


#pandas-DataFrame의 default연산방식은 세로축.
df.sum()


# In[7]:


# 가로의 합(인덱스별 합계)을 구하려면 axis=1를 사용한다.
df.sum(axis=1)


