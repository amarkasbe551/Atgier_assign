# Program to calculate area of circle by using math module function

import math as m

# Input radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = m.pi * (radius ** 2)

# Display the area of the circle
print(f"The area of the circle with radius {radius} is {area}")
