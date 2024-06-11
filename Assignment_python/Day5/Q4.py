# 4. Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters. 
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12


def check(s):
    count_upper = 0
    count_lower = 0
    for char in s:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    print("No. of Uppercase characters:", count_upper)
    print("No. of Lowercase characters:", count_lower)

check('The quick Brow Fox')
