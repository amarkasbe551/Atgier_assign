D = {'a': 10, 'b': 37, 'c': 22, 'd': 33}

number = int(input("Enter a number: "))

filtered_D = {}
for key, value in D.items():
    if value <= number:
        filtered_D[key] = value

print("Output:", filtered_D)
