import re

# Example input string
input_str = """Pune - 412203
Maharashtra.

Welcome to Atgier!"""

# Count the number of digits, alphabets, special characters, white spaces, and lines
digit_count = len(re.findall(r'\d', input_str))
alphabet_count = len(re.findall(r'[a-zA-Z]', input_str))
special_char_count = len(re.findall(r'[^a-zA-Z0-9\s]', input_str))
white_space_count = len(re.findall(r'\s', input_str))
line_count = len(input_str.split('\n'))

# Print the results
print("Total Digits:", digit_count)
print("Total Alphabets:", alphabet_count)
print("Special Characters:", special_char_count)
print("White Spaces:", white_space_count)
print("Number of Lines:", line_count)

