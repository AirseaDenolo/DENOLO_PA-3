# PA3 - PYTHON DATA ANALYSIS (PANDAS)
This repository contains the solutions and Python scripts for a pandas-based programming assignment.

## Problem Overview
This programming assignment focuses on exploring and manipulating a dataset using the Pandas library, a powerful tool for data analysis in Python. The dataset provided (Cars_file.csv) contains various attributes related to different car models.

### Problem 1: Loading and Displaying Data
The first part of the task is aimed at familiarizing users with loading a CSV file into a Pandas DataFrame.
1. Load the provided CSV file into a DataFrame using pandas.
2. Display the first five and last five rows of the dataset.

### Code Implementation
```
import pandas as pd

#Loads the CSV file and reads the Excel file
cars = pd.read_csv('cars.csv')

#Display an output of the first five rows of the resulting cars
print("The First Five Rows:\n", cars.head())

#Display an output of the last five rows of the resulting cars
print("\nThe Last Five Rows:\n", cars.tail())

#Prints to a CSV file or Excel file
cars.to_csv('Denolo_Pandas-P1.py')
```
### Output
![image](https://github.com/user-attachments/assets/13a1770b-79b1-4b41-a169-a03641948410)

### Problem 2: Subsetting, Slicing, and Indexing
The second part of the task focuses on applying more advanced Pandas operations like subsetting, slicing and indexing operations.
Using the DataFrame from Problem 1, extract the following information:
- Display the first five rows with odd-numbered columns.
- Display the row containing the `Model` for 'Mazda RX4'.
- Find how many cylinders the 'Camaro Z28' has.
- Determine the cylinders and gear type for 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.

### Code Implementation
```
import pandas as pd

#Loads the CSV file and reads the Excel file
cars = pd.read_csv('cars.csv')

#Display the first five rows with odd-numbered columns
cars.iloc[:5, ::2] #Selects the first 5 rows and skips every 2 columns to get the odd-numbered columns

#Display the row that contains the model of Mazda RX4
cars.loc[cars['Model'] == 'Mazda RX4']

#Outputs the car model Camaro Z28 and the cyl 8
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]

#Directly filter the specific rows for each car model and concatenate them
models = cars[(cars['Model'] == 'Mazda RX4 Wag') | 
                     (cars['Model'] == 'Ford Pantera L') | 
                     (cars['Model'] == 'Honda Civic')]

#Output only the Model, cyl, and gear columns
print(models[['Model', 'cyl', 'gear']])

#Prints to a CSV file or Excel file
cars.to_csv('Denolo_Pandas-P2.py')
```
### Output
![image](https://github.com/user-attachments/assets/875e6930-ee8a-41c3-bc39-3016b4c114fd)

![image](https://github.com/user-attachments/assets/c4b8f4cb-9166-48f8-8a08-cbc4ca2444a0)

![image](https://github.com/user-attachments/assets/4971c6be-b76d-4587-94b9-17135380db34)

![image](https://github.com/user-attachments/assets/63322262-741d-4930-a431-d942c5afdde9)

## Author
Airsea Grace B. Denolo
