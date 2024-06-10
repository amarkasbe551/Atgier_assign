# Write a program to swap two numbers without using third variable
# Input numbers

num1 = 5
num2 = 10

print(f"Before swapping:-\nnum1={num1}\nnum2={num2}")

# Swapping Logic is here.
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(f"\nAfter swapping:-\nnum1={num1}\nnum2={num2}")

