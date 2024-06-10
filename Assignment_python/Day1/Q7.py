# 7.	Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.
# (Note:if three values are same 2,2,2 then it returns 18)

# Taking inputs:-
a = int(input("Enter Number:-"))
b = int(input("Enter Number:-"))
c = int(input("Enter Number:-"))

if (a == b == c):
    Sum = (a+b+c)
    print(f"Values are equal So, returning three times of their sum :-{Sum*3}")
else:
    print(f"Sum of three number:-{a+b+c}")