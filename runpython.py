#!/usr/bin/env python
# coding: utf-8

# ## Run Python

# In[1]:


import os
from glob import glob

class TreesCounter2:
    @staticmethod
    def count(path, stage, model, cat):
        w = os.path.join(path, stage, model, cat, '*.jpg')
        count = len(glob(w))
        
        return count
    
print(f"tree DR: {TreesCounter2.count('trees', 'train', 'tree', 'DR')}")


# In[ ]:




