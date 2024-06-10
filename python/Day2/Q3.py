# 3. Write a Python program to count the number of even,odd and prime numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 30, 4, 5, 67, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5
# Number of prime numbers: 4

import sympy
def count_prime(*number):
    prime_count = 0
    for num in number:
        if sympy.isprime(num):
            prime_count += 1
    return  prime_count

def count_even(*number):
    even_count = 0
    for num in number:
        if (num % 2 == 0):
            even_count += 1
    return  even_count

def count_odd(*number):
    odd_count = 0
    for num in number:
        if (num % 2 != 0):
            odd_count += 1
    return  odd_count

print("Number of prime numbers:-",count_prime(1, 2, 30, 4, 5, 67, 7, 8, 9))
print("Number of even numbers:-",count_even(1, 2, 30, 4, 5, 67, 7, 8, 9))
print("Number of odd numbers:-",count_odd(1, 2, 30, 4, 5, 67, 7, 8, 9))