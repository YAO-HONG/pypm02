#!/usr/bin/env python
# coding: utf-8

# ## Run Python 2

# In[1]:


import os
from glob import glob

class TreesCounter2:
    @staticmethod
    def count(path, stage, model, cat):
        w = os.path.join(path, stage, model, cat, '*.jpg')
        count = len(glob(w))
        
        return count


# In[2]:


p = input('path: ')
s = input('stage: ')
m = input('model: ')
c = input('category: ')


# In[3]:


print(f'{m} {c}: {TreesCounter2.count(p, s, m ,c)}')


# In[ ]:




