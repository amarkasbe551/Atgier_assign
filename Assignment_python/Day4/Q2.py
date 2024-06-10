# 2. Write a Python program to sort (ascending and descending) a dictionary by value.
# Sample Output:
# Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value :  {0: 0, 2: 1, 1: 2,  4: 3,  3: 4}
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

from operator import itemgetter
original_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Sort in ascending order by value
ascending_dict = dict(sorted(original_dict.items(), key=itemgetter(1)))

# Sort in descending order by value
descending_dict = dict(sorted(original_dict.items(), key=itemgetter(1), reverse=True))

print("Original dictionary:", original_dict)
print("Dictionary in ascending order by value:", ascending_dict)
print("Dictionary in descending order by value:", descending_dict)

