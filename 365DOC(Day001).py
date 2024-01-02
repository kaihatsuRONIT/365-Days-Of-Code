#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Solution:
    # @param A : string
    # @return a strings
    def solve(A):
        return " ".join(A.split()[::-1])
    print(solve("hello world"))


# In[ ]:




