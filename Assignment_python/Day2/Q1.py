# Write a Python program to find those numbers which are divisible by 7, 5 , 2 between 1500 and 2700 (both included).
# Take the range as(1500, 2701)

for num in range(1500,2701):
    if (num % 7 == 0) and (num % 5 == 0) and (num % 2 == 0):
        print("values are:-",num)