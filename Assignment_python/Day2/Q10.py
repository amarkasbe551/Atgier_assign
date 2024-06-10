# 10. Write a Python program to remove and print every third consecutive number from a list.

def rearrange_digits(numbers):
    return numbers[::1] + numbers[::-1]

# Example list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function to rearrange the digits
rearranged_numbers = rearrange_digits(numbers)

# Print the rearranged digits
print("Rearranged digits:", rearranged_numbers)

