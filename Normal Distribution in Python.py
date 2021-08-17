#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import stats


# In[2]:


#stats.norm.cdf(x,loc=mean,scale=std.dev)          
stats.norm.cdf(680,loc=711,scale=29)                 #calculation for normal distribution


# In[ ]:


#Normal Distribution Calculation


# In[3]:


import pandas as pd
import numpy as np


# In[ ]:


#Importing both the files


# In[8]:


beml_df=pd.read_csv("C:/Users/saniyakhan/Downloads/BEML.csv")


# In[9]:


beml_df


# In[10]:


glaxo_df=pd.read_csv("C:/Users/saniyakhan/Downloads/GLAXO.csv")


# In[11]:


glaxo_df


# In[ ]:


#Get the closing prices of both the stocks along with the date       
#Gain= Closing Price - Closing Price / Closing Price


# In[21]:


beml_df=beml_df[['Close','Date']]
beml_df


# In[23]:


glaxo_df=glaxo_df[['Close','Date']]
glaxo_df


# In[ ]:


#The dataframe have a date column,so we can create a DatetimeIndex index from this column Date. It will ensure that the rows are
#sorted by time in ascending order
#Set the date as index for the dateframe to calculate gains


# In[27]:


beml_df=beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))
beml_df


# In[28]:


glaxo_df=glaxo_df.set_index(pd.DatetimeIndex(beml_df['Date']))
glaxo_df


# In[ ]:





# In[30]:


import matplotlib.pyplot as plt
import seaborn as sn
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#Plot the price against time for Glaxo Stock


# In[31]:


plt.plot(glaxo_df.Close);
plt.xlabel('Time');
plt.ylabel('Close Price');


# In[32]:


plt.plot(beml_df.Close);
plt.xlabel('Time');
plt.ylabel('Close Price');


# In[ ]:


#Create the gain column using pct_change() method
#Gain=Closing price(t)-Closing Price(t-1)/Closing Price(t-1)


# In[36]:


beml_df['Gain']=beml_df.Close.pct_change(periods=1)     #here pct_change is the formula & periods is the daily basis calculation
beml_df


# In[38]:


glaxo_df['Gain']=glaxo_df.Close.pct_change(periods=1)     #here pct_change is the formula & periods is the daily basis calculation
glaxo_df


# In[ ]:


#Drop the first row since its NaN


# In[41]:


beml_df=beml_df.dropna()         #drop the missing values it will drop the wole row
beml_df


# In[43]:


glaxo_df=glaxo_df.dropna()         #drop the missing values it will drop the wole row
glaxo_df


# In[ ]:


#Plot the Gains


# In[46]:


plt.figure(figsize=(8,6));
plt.plot(beml_df.index,beml_df.Gain);
plt.xlabel('Time');
plt.ylabel('Gain');


# In[48]:


plt.figure(figsize=(8,6));
plt.plot(glaxo_df.index,glaxo_df.Gain);
plt.xlabel('Time');
plt.ylabel('Gain');


# In[50]:


sn.distplot(beml_df.Gain,label='Beml');
plt.xlabel('Gain');
plt.ylabel('Density');
plt.legend;


# In[ ]:


#To find mean and standard deviation


# In[51]:


print('Mean:',round(beml_df.Gain.mean(),4))


# In[52]:


print('Standard Deviation:',round(beml_df.Gain.std(),4))


# In[53]:


print('Mean:',round(glaxo_df.Gain.mean(),4))


# In[54]:


print('Standard Deviation:',round(glaxo_df.Gain.std(),4))


# In[ ]:





# In[ ]:


from scipy import stats


# In[ ]:


#Probability of making 2% loss or higher in Glaxo file


# In[55]:


stats.norm.cdf(-0.02,
loc=glaxo_df.Gain.mean(),
scale=glaxo_df.Gain.std())


# In[ ]:


#Probability of making 2% high or higher in Glaxo file


# In[56]:


1-stats.norm.cdf(-0.02,
loc=glaxo_df.Gain.mean(),
scale=glaxo_df.Gain.std())


# In[ ]:




