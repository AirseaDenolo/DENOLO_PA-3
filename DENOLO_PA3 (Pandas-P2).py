#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 2

# In[121]:


import pandas as pd

#Loads the CSV file and reads the Excel file
cars = pd.read_csv('cars.csv')

#Display the first five rows with odd-numbered columns
cars.iloc[:5, ::2] #Selects the first 5 rows and skips every 2 columns to get the odd-numbered columns


# In[125]:


#Display the row that contains the model of Mazda RX4
cars.loc[cars['Model'] == 'Mazda RX4']


# In[123]:


#Outputs the car model Camaro Z28 and the cyl 8
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]


# In[127]:


#Directly filter the specific rows for each car model and concatenate them
models = cars[(cars['Model'] == 'Mazda RX4 Wag') | 
                     (cars['Model'] == 'Ford Pantera L') | 
                     (cars['Model'] == 'Honda Civic')]

#Output only the Model, cyl, and gear columns
print(models[['Model', 'cyl', 'gear']])


# In[129]:


#Prints to a CSV file or Excel file
cars.to_csv('Denolo_Pandas-P2.py')


# In[ ]:




