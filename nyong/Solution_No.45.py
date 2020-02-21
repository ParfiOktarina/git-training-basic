#!/usr/bin/env python
# coding: utf-8

# In[5]:


def is_pentagonal(p):
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


# In[6]:


def is_hexagonal(h):
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False


# In[7]:


i = 286


# In[8]:


while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print (triangle)
        break
    i += 1

