# 5. Find out the size of the Employee, Department and location dataset, and write a fuction to create and return a dictionary.

import pandas as pd

employ = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\employees.csv")
depart = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\departments.csv")
loc = pd.read_csv(r"C:\Users\ajayk\Downloads\employee_data\employee_data\locations.csv", error_bad_lines=False)

# Function to calculate sizes and return as a dictionary
def dataset_sizes():
    sizes_dict = {}
    
    # Calculate size for each DataFrame
    sizes_dict['Employee'] = employ.size
    sizes_dict['Department'] = depart.size
    sizes_dict['Location'] = loc.size
    
    return sizes_dict

# Call the function to get sizes
sizes = dataset_sizes()
print(employ.head(2))
print("****************************************************************")
print(depart.head(2))
print("****************************************************************")
print(loc.head(2))
print("****************************************************************")
print(f"Size of the Employee, Department and location dataset:-\n{sizes}")