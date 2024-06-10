# 3.Write a Python program to check whether a given key already exists in a dictionary. Ask the user to input a Key to be searched.
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# Sample Output:
# Key is present in the dictionary                                                                              
# Key is not present in the dictionary

key = int(input("Enter Key Value:- "))

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
if key in d.keys():
    print(f"{key} :- Key is present in the dictionary")
else:
    print(f"{key} :- Key is not present in the dictionary")


