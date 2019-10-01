#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
import numpy as np
df['timemgmt'] = np.where((df['exercise']>3)
        & (df['hours'] > 17),'Busy', 'Not Busy')
df.tail(10)


# In[ ]:




