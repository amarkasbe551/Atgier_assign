
# 1. Write a Python program to generate a random alphabetical string, random value between two integers (inclusive) and
# a random multiple of 7 between 0 and 70.
import random
import string


random_alpha_string = ''.join(random.choices(string.ascii_lowercase, k=10))
print("Random alphabetical string:", random_alpha_string)

random_value = random.randint(5, 15)
print("Random value between 5 and 15:", random_value)

random_multiple_of_seven = random.randint(0, 10) * 7
print("Random multiple of 7 between 0 and 70:", random_multiple_of_seven)