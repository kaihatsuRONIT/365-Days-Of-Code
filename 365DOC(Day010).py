#!/usr/bin/env python
# coding: utf-8

# In[1]:


def solve(A, B):
        topLeft = min(A, B) - 1
        
        bottomRight = 8 - max(A, B)
        
        topRight = min(A, 9-B) -1
        
        bottomLeft = 8 - max(A, 9-B) 
        
        return (topLeft + topRight + bottomRight + bottomLeft)
    
solve(5,2)


# In[ ]:




