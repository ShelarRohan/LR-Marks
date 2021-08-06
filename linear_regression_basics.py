#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[2]:


# Importing dataset and storing it in a db variable. 

db = pandas.read_csv("marks.csv")


# In[3]:


db


# We can do similar operations like numpy over here in pandas.

# In[4]:


# Feature 
# Independent Variable
x = db["hours"]


# In[5]:


x = x.values


# In[6]:


x.shape


# In[7]:


x = x.reshape(4,1)


# In[8]:


# Target Variable
# Dependent Variable ---> As marks is dependent on x i.e no of hours
y = db["marks"]


# In[9]:


y


# In[10]:


# Load the module and function
from sklearn.linear_model import LinearRegression


# In[11]:


mind = LinearRegression()


# Now, train the model 

# In[12]:


mind.fit(x,y)


# In[15]:


# To predict 

mind.predict([[5]])


# In[16]:


# To save any model 
# import joblib 

import joblib


# In[17]:


joblib.dump(mind,'marks_model.pkl')


# In[18]:


# Loading model 
import joblib
model = joblib.load('marks_model.pkl')


# In[20]:


model.predict([[8]])


# In[ ]:




