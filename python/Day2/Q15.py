# Take input string from the user
input_str = input("Enter a string: ")

# Convert to uppercase
upper_str = ''
for char in input_str:
    if 'a' <= char <= 'z':
        upper_str += chr(ord(char) - 32)
    else:
        upper_str += char

# Convert to lowercase
lower_str = ''
for char in input_str:
    if 'A' <= char <= 'Z':
        lower_str += chr(ord(char) + 32)
    else:
        lower_str += char

# Print the results
print("Uppercase:", upper_str)
print("Lowercase:", lower_str)
