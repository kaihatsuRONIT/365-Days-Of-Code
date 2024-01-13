#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
def isPrime(A):
        x=int(math.sqrt(A))
        if(A==1):
            return 0
        for i in range(2,x+1):
            if (A%i==0):
                return 0
        return 1
isPrime(79)
    


# In[ ]:





# In[ ]:




