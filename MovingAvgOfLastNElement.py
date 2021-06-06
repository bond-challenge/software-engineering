#!/usr/bin/env python
# coding: utf-8

# We need to design in a way that when a new element in a list or array comes then we can compute 
# avg of last N elements in the stream in O(1) time. 
# For example, if new streams 3 comes after the last stream 0, then moving avg would be (-3+0+3)/3 = 0.0.
# We can use the formula avg=(n*avg+new_element)/(n+1) upto N elements.

# In[14]:


list_data = [13, 21, 38, 14, 9, 15, 50, 56]
window_size = 3

i = 0
moving_averages = []
while i < len(list_data ) - window_size + 1:
    this_window = list_data [i : i + window_size]


    window_average = sum(this_window) / window_size
    moving_averages.append(window_average)
    i += 1

print(moving_averages)


# In[ ]:




