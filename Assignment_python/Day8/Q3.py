# 3. Read Employee data from file and create the dataframe. select employee_id, first_name, last_name, hire_date. 

import pandas as pd

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
print(employ.head(3))
col_employ = employ[["employee_id", "first_name", "last_name", "hire_date"]]
print(col_employ.head(3))

