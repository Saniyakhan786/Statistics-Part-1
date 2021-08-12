#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Import all the necessary library by usning the import function if you do not have an library install it using pip function (pip install library name)


# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns


# In[ ]:


# To Import Dataset


# In[2]:


df = pd.read_csv("C:/Users/saniyakhan/Downloads/Salaries.csv")


# In[3]:


df.head()   #default first five records


# In[4]:


df.head(35)   #for specific number of records


# In[6]:


df['rank'].dtype     #particular record datatype


# In[8]:


df.dtypes           #for all records datatype


# In[9]:


df.info()     #Information about the dataset


# In[12]:


df.size      #total records of rows and columns


# In[13]:


df.ndim       #number of dimensions


# In[14]:


df.describe()         #range of records


# In[18]:


df.max()     #maximum of each column


# In[19]:


df.min()     #minimum of each column


# In[20]:


df.mean()    #mean of all the column


# In[21]:


df.count()    #no of counts in record


# In[22]:


df.head().mean()   #mean of first 5 records


# In[23]:


df.head(12).mean() #mean for specific records


# In[31]:


df[['salary']].mean()


# In[ ]:


#Groupby i.e Aggregate Function


# In[32]:


df_rank = df.groupby(['rank'])    #group data using rank


# In[33]:


df_rank.mean()        #calculate mean value for each numeric value per each group


# In[34]:


df.groupby('rank')[['salary']].mean()    #the column by which we want to group then the operation


# In[35]:


df.groupby('rank')[['salary','discipline']].mean()


# In[37]:


df.groupby((['rank']),sort=False)[['salary']].mean()


# In[38]:


grouped=df.groupby('rank')


# In[39]:


type(grouped)


# In[ ]:


#Data frame Filtering
#Any boolean operator can be used to subset the data


# In[42]:


df_sub=df[df['rank']> 'salary']


# In[43]:


df_f=df[df['rank']=='salary']


# In[ ]:


#Dataframe Slicing
#Using integer location method i.e iloc


# In[44]:


df.iloc[0]         #First row of a data frame


# In[ ]:


df.iloc[i]     #ith row


# In[46]:


df.iloc[-1]       #last row


# In[47]:


df.iloc[:, 0]      #first column


# In[48]:


df.iloc[:, -1]     #first column


# In[49]:


df.iloc[0:7]      #first 7 column


# In[52]:


df.iloc[:,0:2]       #first 2 columns


# In[53]:


df.iloc[1:3, 0:2]       #first and second row and first 2 columns


# In[54]:


df.iloc[[0,5],[1,3]]       #first and fifth row


# In[ ]:


####PANDAS#####


# In[ ]:


#Aggragte functions in Pandas


# In[55]:


df[['rank','salary']].agg(['min','mean','max'])        #aggregate function by columns 


# In[56]:


df.describe()   #basic statistics


# In[57]:


df.min()
df.max()


# In[58]:


df.mean()


# In[60]:


df.median()


# In[61]:


df.mode()


# In[62]:


df.var()


# In[63]:


df.std()


# In[64]:


df.sem()


# In[65]:


df.skew()


# In[66]:


df.kurt()


# In[ ]:




