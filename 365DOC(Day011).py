#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


def solve(A, B, C):
        fine=0
        if(B%2==0):
            for i in A:
                if(i%2!=0):
                    fine=fine+C
            return fine
        elif(B%2!=0):
            for i in A:
                if(i%2==0):
                    fine=fine+C
            return fine
solve([0,3,6,2],29,10000)


# In[ ]:




