# 2. Write a Python function to perform sum of all the elements of a list 
# Sample List : [8, 2, 3, 0, 7]

total = 0

def sum(li):
    global total 
    for arg in li:
        total += arg
    return total

print(sum([8, 2, 3, 0, 7]))