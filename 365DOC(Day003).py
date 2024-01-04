#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[9]:


def solve(A):
        # Count the occurrences of each character in the string
        char_count = {}
        for char in A:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Count the number of characters with odd occurrences
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1

        # If there is at most one character with odd occurrences, it is possible to form a palindrome
        return 1 if odd_count <= 1 else 0
    
    


# In[ ]:




