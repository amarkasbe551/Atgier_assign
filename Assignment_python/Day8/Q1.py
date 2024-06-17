# 1. Read Department data from file and create the dataframe.
# Create the dataframe with only department_id,department_name. and print the data.

import pandas as pd

Department = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\departments.csv")
print(Department)