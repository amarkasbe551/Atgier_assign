# 9. Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
for key, value in d1.items():
    if key in d2:
        d2[key] += value
    else:
        d2[key] = value

print("Combined dictionary:", d2)

