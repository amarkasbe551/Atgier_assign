# 8. Write a Python program to compute the distance between the points 
# (x1, y1,z1) and (x2, y2,z2).

import math


x1, y1, z1 = 1, 2, 3
x2, y2, z2 = 4, 5, 6

# Calculate the differences 
dx = x2 - x1
dy = y2 - y1
dz = z2 - z1

# Calculate square of the differences
dx_squared = dx ** 2
dy_squared = dy ** 2
dz_squared = dz ** 2

# Calculate sum of the squares
sum_of_squares = dx_squared + dy_squared + dz_squared

# Calculate square root of the sum of squares to get the distance
distance = math.sqrt(sum_of_squares)

# Print the distance
print("Distance between the points:", round(distance,2))
