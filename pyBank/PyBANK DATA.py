#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Dalit\\OneDrive\\Desktop\\Python Bootcamp\\Python Assignment 1\\Pybank\\budget_data.csv")


# In[9]:


df.head()


# In[12]:


print (df["Date"].count())


# In[13]:


print (df["Profit/Losses"].sum())


# In[81]:


values = df["Profit/Losses"]
sumOfNums= sum(values)
count= len(values)
average = sumOfNums / count
print ("the sum is:", values)
print ("the average of all numbers is:", average)


# In[80]:





# In[ ]:





# In[ ]:




