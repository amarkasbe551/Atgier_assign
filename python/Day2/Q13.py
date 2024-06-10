import inflect

def number_to_words(num):
    p = inflect.engine()
    return p.number_to_words(num)

# Given numbers
numbers = [1976, 641]

# Print numbers in words
for num in numbers:
    print(num, ":", number_to_words(num))
