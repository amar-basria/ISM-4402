#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df = df.sort_values(by=['lname','grade', 'age'],
        ascending=[True, True, True])
df.head()


# In[ ]:




