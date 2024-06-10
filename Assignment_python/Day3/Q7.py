# Write a Python program to shuffle and print a list entered by the user

import random

user_input = input("Enter a list of elements separated by commas: ")
user_list = user_input.split(',')
random.shuffle(user_list)

# Printing the shuffled list
print("Shuffled list:", user_list)
