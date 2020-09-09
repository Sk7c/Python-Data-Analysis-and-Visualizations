#!/usr/bin/env python
# coding: utf-8

# Matplotlib

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[3]:


plt.plot([1,7,9,14])


# In[4]:


plt.plot([1,2,7,8],[1,9,7,14])


# In[5]:


plt.plot([1,2,7,8],[1,9,7,14],'ro')


# In[8]:


a = np.array([[1,2,3,4],[5,6,7,8]])
plt.plot(a[0],a[1],'go')


# In[11]:


plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot(a[0],a[1], 'b--')


# In[16]:


t = np.linspace(0,5,20)

plt.plot(t, t**2, color ='coral', linestyle='--')

plt.plot(t, 4*t, color = 'indigo', linewidth = 2)


# In[21]:


plt.subplot(1,3,1)
plt.plot(t,t,'c--')

plt.subplot(1,3,2)
plt.plot(t,t**2,'b--')

plt.subplot(1,3,3)
plt.plot(t,t**3,'mo')


# In[26]:


grades = {'John' : 90,
          'Susan' : 34,
           'Raj' : 78,
           'Ben' : 89,
           'David' : 45}
plt.bar(range(len(grades)), list(grades.values()), color ='darkturquoise')
plt.xticks(range(len(grades)), list(grades.keys()))
plt.xlabel('Students')
plt.ylabel('Grades')


# In[27]:


x = np.random.randn(1000)
plt.hist(x, color ='seagreen')


# In[ ]:




