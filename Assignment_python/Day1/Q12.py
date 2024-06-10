# List out the different types of type casting in python (e.g. int to float)

# Integer to Float
num_int = 10
num_float = float(num_int)

# Float to Integer
num_float = 3.14
num_int = int(num_float)

# String to Integer or Float
str_num = "10"
num_int = int(str_num)
num_float = float(str_num)

# Integer or Float to String
num_int = 10
num_float = 3.14
str_num_int = str(num_int)
str_num_float = str(num_float)

# String to List
str_value = "hello"
list_value = list(str_value)

# List to String
list_value = ['h', 'e', 'l', 'l', 'o']
str_value = ''.join(list_value)

# Integer to Boolean
num_int = 1
bool_value = bool(num_int)

# Boolean to Integer
bool_value = True
num_int = int(bool_value)

# Displaying the results
print("Integer to Float:", num_float)
print("Float to Integer:", num_int)
print("String to Integer:", num_int)
print("String to Float:", num_float)
print("Integer to String:", str_num_int)
print("Float to String:", str_num_float)
print("String to List:", list_value)
print("List to String:", str_value)
print("Integer to Boolean:", bool_value)
print("Boolean to Integer:", num_int)

