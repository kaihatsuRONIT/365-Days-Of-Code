#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[18]:


list=[]
a = int(input("enter a number:- "))
for i in range(1,a+1):
    if(i%3==0 and i%5==0):
        list.append("FizzBuzz")
    elif(i%3==0):
        list.append("Fizz")
    elif(i%5==0):
        list.append("Buzz")
    else:
        list.append(i)
print(list)


# In[ ]:




