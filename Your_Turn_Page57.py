#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
List = zip(names,grades,bsdegrees,msdegrees,phddegrees)
df = pd.DataFrame(data=List,
columns=['Names','Grades','BS Degress','MS Degrees','PHD Degrees'])
df


# In[11]:


df.std()
df.min()
df.max()
df.quantile(.25)  # first quartile
df.quantile(.5)   # second quartile
df.quantile(.75)  # third quartile
#I have grouped all the summary statistics functions together for reference purposes. 
#But when running the code only the last quantile funtions runs.


# In[ ]:




