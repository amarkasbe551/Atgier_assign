# 5. Check if a set is a subset of another set, using comparison operators and issubset():
# Sample Output:
# x:  {'mango', 'apple'}
# y:  {'mango', 'orange'}
# z:  {'mango'} 

# If x is subset of y
# False
# False
# If y is subset of x
# False
# False

# If y is subset of z
# False
# False
# If z is subset of y
# True
# True

def is_subset_and_comparison(set1, set2):
    # Using comparison operators
    is_subset_comparison = set1 <= set2

    # Using issubset() method
    is_subset_method = set1.issubset(set2)

    return is_subset_comparison, is_subset_method

# Example usage:
x = {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

print("x:", x)
print("y:", y)
print("z:", z)

result_x_y_comparison, result_x_y_method = is_subset_and_comparison(x, y)
result_y_x_comparison, result_y_x_method = is_subset_and_comparison(y, x)
result_z_y_comparison, result_z_y_method = is_subset_and_comparison(z, y)

print("Is x a subset of y using comparison operator?", result_x_y_comparison)
print("Is x a subset of y using issubset() method?", result_x_y_method)
print("Is y a subset of x using comparison operator?", result_y_x_comparison)
print("Is y a subset of x using issubset() method?", result_y_x_method)
print("Is z a subset of y using comparison operator?", result_z_y_comparison)
print("Is z a subset of y using issubset() method?", result_z_y_method)



