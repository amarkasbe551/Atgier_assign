# 6. Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 then return double of the difference.(Print Absolute value of output)
# Sample Output1:
# Enter number :22
# Answer:10
# Sample Output2:
# Enter number :14
# Answer:3

num = int(input("Enter Number:-"))

if num > 17:
    num -= 17
    # Printing the absolute value of the output
    print("Anwser:-",abs(num*2))
else:
    num -= 17
    print("Anwser:-",abs(num))

