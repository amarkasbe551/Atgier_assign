# 5. Write a Python program to calculate the area and volume of a cylinder.

import math


radius = int(input("Enter radius of cylinder:-"))
height = int(input("Enter height of cylinder:-"))

# Calculate lateral surface area of the cylinder
lateral_area = 2 * math.pi * radius * height

# Calculate base area of the cylinder
base_area = math.pi * radius ** 2

# Total surface area of the cylinder
total_area = lateral_area + 2 * base_area

# Calculate volume of the cylinder
volume = math.pi * radius ** 2 * height

# Print the results
print("Area of the cylinder:", round(total_area,2))
print("Volume of the cylinder:", round(volume,2))

