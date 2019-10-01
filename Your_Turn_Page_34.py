#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[5]:


# Create the bin dividers
bins = [0,80,100]
# Create names for the four groups
group_names = ['Fail', 'Pass']


# In[6]:


df['lettergrade'] = pd.cut(df['grade'], bins,
        labels=group_names)
df


# In[ ]:




