# 6. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them
# E.g. 
# input - Adam Samuel
# Output - madA leumaS 

first_nam = input("Enter First Name:-")
last_nam = input("Enter LastMAar Name:-")

print(f"{first_nam[::-1]} {last_nam[::-1]}")