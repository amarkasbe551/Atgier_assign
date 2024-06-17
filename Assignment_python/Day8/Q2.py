# 2. Read countries data from file and create the dataframe. find the object type columns from it.

import pandas as pd

countries = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\countries.csv")
print(countries.info())
object_columns = countries.select_dtypes(include=['object'])
print(object_columns)