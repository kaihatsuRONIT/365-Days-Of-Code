#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solve(A):
        mul=1
        count = 0
        while(A>0):
            x=A%10
            A=A//10
            mul = mul*x
            count+=1
        if(mul == 1 and count == 0):
            return 0   
        return mul
        


# In[ ]:




