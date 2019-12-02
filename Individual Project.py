#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
data= 'datasets/axisdata.csv'
df = pd.read_csv(data)
df.head()


# In[4]:


df['Cars Sold'].mean()


# In[5]:


df['Cars Sold'].max()


# In[6]:


df['Cars Sold'].min()


# In[18]:


Gender_CarsSold= pd.pivot_table(df,values='Cars Sold', index='Gender')
Gender_CarsSold


# In[9]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[10]:


df['Years Experience'].mean()


# In[12]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[17]:


SalesTraining_CarsSold=pd.pivot_table(df,values='Cars Sold', index='SalesTraining')
SalesTraining_CarsSold


# In[20]:


SalesTraining_CarsSold.plot(kind='bar')


# In[22]:


AverageHoursWorked_Gender = pd.pivot_table(df,values='Hours Worked', index='Gender')
AverageHoursWorked_Gender


# In[23]:


AverageHoursWorked_Gender.plot(kind='bar')


# In[ ]:




