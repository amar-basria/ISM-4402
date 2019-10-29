#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
get_ipython().magic(u'matplotlib inline')


Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[7]:


df.hist()


# In[8]:


df.hist(column="age")


# In[9]:


df.hist(column="age", by="gender")


# In[ ]:




