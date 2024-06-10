# 8. Write a Python program to get unique values from a list.

li = [1,2,3,4,3,2,1,3,5,7,4,3,4,67,8,4,2,3,4,4,43,23,4,5,7,6,543,2,1,1,3,3,89,78,65,45,27]

# Converting list to set to get unique value only.
uniq = list(set(li))

print(f"Orginal list :- {li}")
print(f"Unique value only :- {uniq}")