# 4. Read Employee data from file and create the dataframe.
# Find the unique hire_dates from the dataframe as list.

import pandas as pd

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
print(employ.head(3))
unique_hire_dates = employ['hire_date'].unique().tolist()
print(unique_hire_dates)