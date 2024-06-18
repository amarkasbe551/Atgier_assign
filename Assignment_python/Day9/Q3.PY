# 3. Create a bar chart to show the number of employees per country 

import pandas as pd
import matplotlib.pyplot as plt

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
countries = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\countries.csv")
regions = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\regions.csv")
depart = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\departments.csv")
loc = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\locations.csv", error_bad_lines=False)
print(employ.head(5))
print("***********************************************")
print(countries.head(5))
print("***********************************************")
print(regions.head(5))
print("***********************************************")
print(depart.head(5))
print("***********************************************")
print(loc.head(5))
print("***********************************************")

employee_details = employ.merge(depart, on='department_id').merge(loc, on='location_id').merge(countries, on='country_id').merge(regions, on='region_id')
employees_per_country = employee_details.groupby('country_name').size().reset_index(name='employee_id')
print(employees_per_country)


plt.figure(figsize=(10, 6)) 
plt.bar(employees_per_country['country_name'], employees_per_country['employee_id'], color='skyblue')
# Adding titles and labels
plt.title('Number of Employees per Country')
plt.xlabel('Country')
plt.ylabel('Number of Employees')
plt.show()