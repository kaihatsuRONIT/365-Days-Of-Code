#!/usr/bin/env python
# coding: utf-8

# In[4]:


def solve(A):
    zeros = []
    ones = []
    for i in A:
        if(i%2==0):
            zeros.append(i)
        else:
            ones.append(i)
    for i in ones:
        zeros.append(i)
    return zeros
print(solve([1,0,0,1,0,1,1,0,1,1,1,0,0,0]))
        


# In[ ]:




