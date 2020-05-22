#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data1 = pd.read_csv('./rotten_tomatoes_reviews1.csv')
data2 = pd.read_csv('./rotten_tomatoes_reviews2.csv')
data = pd.concat([data1, data2])
data.to_csv('rotten_tomatoes_reviews.csv')


# In[ ]:




