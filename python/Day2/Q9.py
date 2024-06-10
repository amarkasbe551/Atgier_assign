# 9. Write a Python program to count the number occurrence of a specific character in a string


def count_and_character(string, char):
    count = 0
    for c in string.lower():
        if c == char:
            count += 1
    return count, char

# Example string
string = "Amar Kasbe"
# Character to count
char = "a"

# Call the function and print the result
count, character = count_and_character(string, char)
print("Number of occurrences of '{}' in '{}': {}".format(character, string, count))
