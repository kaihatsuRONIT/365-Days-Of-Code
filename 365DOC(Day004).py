#!/usr/bin/env python
# coding: utf-8

# In[10]:


def solve(A, B):
    count=0
    for i in A:
        if(i<=B):
            count+=1
    return count
A=[10,20,30,40,50]
B=31
print(solve(A,B))
        


# In[ ]:




