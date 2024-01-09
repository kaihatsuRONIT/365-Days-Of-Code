#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[15]:


def solve(A):
        res=[0,0]
        countneg=0
        countpos=0
        for i in A:
            if(i<0):
                countneg= countneg+1
                res[1] = countneg
            elif(i>0):
                countpos+=1
                res[0] = countpos
            else:
                pass
        return res
solve([8,3,2,5,-2,5,-4,-6,-8])


# In[ ]:





# In[ ]:





# In[ ]:




