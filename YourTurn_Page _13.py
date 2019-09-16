#!/usr/bin/env python
# coding: utf-8

# In[10]:


path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""
import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[9]:


import pandas as pd
import numpy as np
import glob

all_data= pd.DataFrame()
for f in glob.glob("datasets/weekly_call_data/weekdata*.xlsx"):
    df=pd.read_excel(f)
    all_data = all_data.append(df,ignore_index = True)
all_data.describe()


# In[ ]:




