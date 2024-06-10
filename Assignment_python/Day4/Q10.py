# 10. Write a Python program to find the highest of 3 values for corresponding keys in a dictionary. 
# D ={‘a’:10,’b’:37,’c’:22,’d’:33,’e’:45,’f’:9,’g’:88,’h’:63,’i’:98,’j’:12}
# Input any 3 keys from given dictionary ex: a,b,c
# Then output should be b:37

D = {'a': 10, 'b': 37, 'c': 22, 'd': 33, 'e': 45, 'f': 9, 'g': 88, 'h': 63, 'i': 98, 'j': 12}

keys = input("Enter any 3 keys from the given dictionary (comma-separated): ").split(',')

highest_value = max(D[key] for key in keys)

print("The highest value among the input keys is:", highest_value)

