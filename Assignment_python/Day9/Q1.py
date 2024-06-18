# 1. Read the data for Employee check the null values for the required data files.
# Select the Employee details for employee as Employee ID, Name (First_Name Last_Name), email, hire_date, job_title and department_name.

import pandas as pd

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
depart = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\departments.csv")
job = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\jobs.csv")

# Check null values in each DataFrame
print("Null values in employees DataFrame:")
print(employ.isnull().sum())

print("\nNull values in departments DataFrame:")
print(depart.isnull().sum())

print("\nNull values in jobs DataFrame:")
print(job.isnull().sum())

# Merge dataframes to get complete information
employee_details = employ.merge(job, on='job_id').merge(depart, on='department_id')

# Select required columns
employee_details = employee_details[['employee_id', 'first_name', 'last_name', 'email', 'hire_date', 'job_title', 'department_name']]

# Display the selected details
print(employee_details)

