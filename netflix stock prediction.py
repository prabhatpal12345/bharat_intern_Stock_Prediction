#!/usr/bin/env python
# coding: utf-8

# # Position : Data Science Internship
# 
Project Name (Task 1): Stock Market Prediction for NetflixObjective of the Project :

1) Volume ofStock Trade.
2) Netflix Stock Price - High, Open, Close.
3) Netflix Stock Price -Day, Month, Year Wise.
4) Top-5 Dates with Highest Stock Price.
5) Top-5 Dates with Lowest Stock Price.
# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datetime import datetime


# In[7]:


df = pd.read_csv("Netflix.csv")


# In[9]:


df.head()


# In[8]:


sns.set(rc={'figure.figsize':(10,5)})


# In[9]:


df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.head()


# In[11]:


sns.lineplot(x=df.index, y=df['Volume'],label ='Volume')
plt.title('Volume f stock versus time')


# In[12]:


df.plot(y=['High','Close' ,'Open'] ,title ='Netflix Stock Price')


# In[16]:


fig, (ax1 ,ax2 ,ax3) = plt.subplots(3, figsize = (15,10))
df.groupby(df.index.day).mean().plot(y = 'Volume' ,ax = ax1, xlabel ='Day')
df.groupby(df.index.day).mean().plot(y = 'Volume' ,ax = ax2, xlabel ='Month')
df.groupby(df.index.day).mean().plot(y = 'Volume' ,ax = ax3, xlabel ='Year')


# # Dates With highest Stock Price

# In[17]:


df


# In[18]:


a = df.sort_values(by ='High',ascending =False).head(5)
a['High']


# In[19]:


df


# In[21]:


b = df.sort_values(by ='Low',ascending =True).head(5)
b['Low']


# In[28]:


fig,axes = plt.subplots(nrows =1, ncols =2, sharex =True, figsize =(12,5))
fig.suptitle('High and Low Values Stock per period of time',fontsize =18)
sns.lineplot(ax = axes[0], y = df['High'],x =df.index, color ='green')
sns.lineplot(ax = axes[1], y = df['Low'],x =df.index, color ='red')


# In[ ]:




