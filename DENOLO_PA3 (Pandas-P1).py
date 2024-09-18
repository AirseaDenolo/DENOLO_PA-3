#!/usr/bin/env python
# coding: utf-8

# # PROBLEM 1

# In[117]:


import pandas as pd

#Loads the CSV file and reads the Excel file
cars = pd.read_csv('cars.csv')

#Display an output of the first five rows of the resulting cars
print("The First Five Rows:\n", cars.head())

#Display an output of the last five rows of the resulting cars
print("\nThe Last Five Rows:\n", cars.tail())

#Prints to a CSV file or Excel file
cars.to_csv('Denolo_Pandas-P1.py')

