#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd


# Read csv file
# 

# In[2]:


titanic = pd.read_csv('Titanic.txt', sep='\t')
print(titanic.head())


# Select age 

# In[3]:


titanic['age']


# Select age and passenger class

# In[4]:


titanic[['age','pclass']]


# Select children in second passenger class 

# In[5]:


titanic[(titanic.age=='child') & (titanic.pclass=='2nd')]


# Select passenges from 320 to 329 using list slicing

# In[6]:


titanic[320:330]


# Count of passengers based on age group

# In[7]:


by_age = titanic.groupby('age')
by_age.size()


# Count of passengers by gender

# In[8]:


by_sex = titanic.groupby('sex')
by_sex.size()


# Gender count of passengers based on survival rates

# In[11]:


print(titanic.groupby(['sex']).size())
print(titanic.groupby(['survived','sex']).size())


# In[ ]:





# In[ ]:




