# 5. Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam

def ip():
    name = input("Enter Your Name:- ")
    print(check(name))

def check(nam):
    if nam.lower() == nam.lower()[::-1]:
        return f"{nam} Is Palindrome"
    else:
        return f"{nam} Is Not Palindrome"

ip()