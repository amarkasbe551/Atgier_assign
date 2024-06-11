# 3.  Write a Python function to check whether a number falls in a given range
# (Note: Ask the user for the range and number.)


def ip():
    num = int(input("Enter Number:- "))
    li = list((int, input("Enter Range Of Numbers (space-separated): ").split()))
    print(check(num, li))

def check( num, li):
    if num in li:
        return f"{num} is in given Range {li}"
    else:
        return f"{num} is not in given Range {li}"
    
ip()


