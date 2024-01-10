#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[20]:


A="HEmlo@#0001"
l, u, p, d = 0, 0, 0, 0
if (len(A) >= 8  and len(A)<=15):
    for i in A: 
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        # counting digits
        if (i.isdigit()):
            d+=1
        # counting the mentioned special characters
        if(i=='@'or i=='#' or i=='%' or i=='&'or i=='!' or i=='$' or i=='*'):
            p+=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(A)):
    print("valid password")
            
else:
    print("invalid password")


# In[ ]:





# In[ ]:





# In[ ]:




