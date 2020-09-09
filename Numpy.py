#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[17]:


n = np.array([1,2,3])
print (n)
print (n.shape)
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(a)
print(a[0,2])


# In[23]:


a = np.zeros((2,3))
print(a)


# In[25]:


b = np.ones((1,2))
print(b)


# In[27]:


c = np.full((2,3), 7)
print(c)


# In[30]:


d = np.random.random((2,2)); print(d)


# In[41]:


a = np.array([[1,2,3,0],
              [4,5,6,0],
              [7,8,9,0]])
print(a)
b = a[:2, 1:4]
print(b)

print (a[0,1])
b[0,1] = 34
print(b)
print(a[0,2])


# In[3]:


a = np.array([[1,2,3,0],
              [4,5,6,0],
              [7,8,9,0]])
print(a)
print(a > 2)
print(a[a>2])


# In[16]:


x = np.array ([[2,3],[4,5]])
y = np.ones((2,2))
print(x)
print(y)
print(x+y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.sum(x))
print(np.sum(x, axis =0))
print(np.sum(x, axis =1))


# PANDAS
# 

# In[1]:


import pandas as pd


# In[2]:


s = pd.Series(['jon','smith','berry','Ron'])
print(s)
print(s[0])

print(s[1:4])

print(s[[0,1,3]])


# In[38]:


s = pd.Series(['jon','smith','berry','Ron'])
param = s != 'jon'
print(s[param])


# In[5]:


d = {'New York' : 1300,
    'Chicago' : 900,
     'San Francisco'  : 1100,
     'Austin' : 450}
print(d)
cities = pd.Series(d)
print(cities)


# In[41]:


cities[['Chicago', 'San Francisco']]


# In[42]:


cities[cities< 1000]


# In[7]:


cities[cities< 1000] =750
print(cities)


# In[10]:





# In[11]:





# In[12]:





# In[13]:





# In[ ]:




