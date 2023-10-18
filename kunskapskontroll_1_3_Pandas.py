#!/usr/bin/env python
# coding: utf-8

# # Pandas
# Read "10 minutes to Pandas": https://pandas.pydata.org/docs/user_guide/10min.html before solving the exercises.
# We will use the data set "cars_data" in the exercises below. 

# In[1]:


# Importing Pandas. 
import pandas as pd


# ### Explain what a CSV file is.

# it is a textfile with data in colums and rows, separated by design (as tab or ; or ; or space etc

# ### Load the data set "cars_data" through Pandas. 

# In[2]:


# When reading in the data, either you have the data file in the same folder as your python script
# or in a seperate folder.

# Code below can be ran if you have the data file in the same folder as the script
# cars = pd.read_csv("cars_data.csv")

# Code below can be ran if you have the data file in another script. 
# Notice, you must change the path according to where you have the data in your computer. 
# pd.read_csv(r'C:\Users\Antonio Prgomet\Documents\ec_utbildning\kursframstallning\ds23\python_stat\exercises\numpy_matplot_pandas\cars_data.csv')


# In[3]:


cars = pd.read_csv("cars_data.csv")


# ### Print the first 10 rows of the data. 

# In[4]:


print(cars.head(10))


# ### Print the last 5 rows. 

# In[5]:


print(cars.tail(5))


# ### By using the info method, check how many non-null rows each column have. 

# In[6]:


#cars.count()
cars.info()


# ### If any column has a missing value, drop the entire row. Notice, the operation should be inplace meaning you change the dataframe itself.

# In[7]:


cars.dropna(inplace=True)
cars.count()


# ### Calculate the mean of each numeric column. 

# In[37]:


print(cars.mean(numeric_only=True))


# ### Select the rows where the column "company" is equal to 'honda'. 

# In[ ]:


print(cars.loc[cars['company'] == 'honda'])


# ### Sort the data set by price in descending order. This should *not* be an inplace operation. 

# In[ ]:


cars2=cars.sort_values('price', ascending=False)
print(cars.head(10))
print(cars2.head(10))


# ### Select the rows where the column "company" is equal to any of the values (audi, bmw, porsche).

# In[ ]:


print(cars[(cars['company'] == 'audi') | (cars['company'] == 'bmw') | (cars['company'] == 'porsche')] )
#or use isin.


# ### Find the number of cars (rows) for each company. 

# In[10]:


#print(cars.groupby(["company"]).count())
#print(cars["company"].values)
print("Below are the number of rows under each brand of car:\n",cars["company"].value_counts())
#cars[["company","body-style"]].value_counts()


# ### Find the maximum price for each company. 

# In[35]:


#print(cars)

print(cars.groupby("company")[["price"]].max())


# In[ ]:




