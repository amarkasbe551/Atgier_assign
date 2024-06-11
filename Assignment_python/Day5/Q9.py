# 9. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
# add another function which can calculate the sum of common multiples of 3 and 5
# For example, if limit is 30, it should return the sum of all elements
# 3, 5, 6, 9, 10, 12, 15, 18, 20,21,24,25,27,30.
# Sum of all common multiples :
# 15,30

def sum_multiples_3_5(limit):
    total = 0
    for num in range(limit + 1):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total

def sum_common_multiples_3_5(limit):
    total = 0
    for num in range(limit + 1):
        if num % 3 == 0 and num % 5 == 0:
            total += num
    return total

def ip():
    limit = int(input("Enter limit value: "))
    print("Sum of multiples of 3 and 5:", sum_multiples_3_5(limit))
    print("Sum of common multiples of 3 and 5:", sum_common_multiples_3_5(limit))

ip()
