# 1. To define a roots() to calculate roots of a quadratic equation, ax2 + bx +c which takes a ,b and c as arguments.

import math

def roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return root1, root2

# Example usage
a = 10
b = -35
c = 25

print("Roots:", roots(a, b, c))
