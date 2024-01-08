#!/usr/bin/env python
# coding: utf-8

# In[13]:


A=int(input("enter a year :- "))
if(A%400==0 and A%100==0):
    print("leapyear")
elif( A%4==0 and A%100!=0):
    print("leapyear")
else:
    print("not a leap year")


# In[ ]:





# In[ ]:




