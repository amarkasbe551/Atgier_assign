# 1.Write a Python program to iterate over dictionaries using for loops.
# Original Dictionary
# d = {'x': 10, 'y': 20, 'z': 30} 
# Expected Output
# x -> 10
# y -> 20
# z -> 30

d = {'x': 10, 'y': 20, 'z': 30} 

for i,j in d.items():
    print(i,"->",j)
