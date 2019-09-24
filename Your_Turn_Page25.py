#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
location="datasets/gradedata.csv"
df=pd.read_csv(location)
df.loc[(df['grade'] <= 0,'grade')] = 0
df


# In[ ]:




