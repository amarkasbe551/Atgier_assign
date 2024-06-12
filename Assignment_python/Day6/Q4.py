# 4. Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2,2)

    def perimeter(self):
        return round(2 * math.pi * self.radius,2)

# Creating an instance of the Circle class with radius 5
circle = Circle(5)

# Calculating and printing the area of the circle
print("Area of the circle:", circle.area())

# Calculating and printing the perimeter of the circle
print("Perimeter of the circle:", circle.perimeter())
