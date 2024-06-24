# 4. Create a pie chart to show the percentage of employees working in each department.

import pandas as pd
import matplotlib.pyplot as plt

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
depart = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\departments.csv")
print(employ.head(5))
print("***********************************************")
print(depart.head(5))
print("***********************************************")
employee_details = employ.merge(depart, on='department_id')
print(employee_details.head(5))
print("***********************************************")
employees_per_department = employee_details.groupby('department_name').size().reset_index(name='employee_id')
# Rename the 'employee_id' column to 'count_employee'
employees_per_department = employees_per_department.rename(columns={'employee_id': 'count_employee'})
# Calculate percentage of employees in each department
employees_per_department['percentage'] = (employees_per_department['count_employee'] / employees_per_department['count_employee'].sum()) * 100
print(employees_per_department)
print("***********************************************")

# Plotting the pie chart
plt.figure(figsize=(8, 6))  # Optional: adjust the figure size
plt.pie(employees_per_department['percentage'], labels=employees_per_department['department_name'], autopct='%1.1f%%', startangle=140)

# Adding titles
plt.title('Percentage of Employees per Department')

# Display the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.show()
print("Hello " + "3")