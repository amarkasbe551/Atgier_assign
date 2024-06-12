def add_variables(a, b):
    try:
        result = a + b
    except TypeError:
        if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)):
            result = str(a) + str(b)
        elif isinstance(a, str) or isinstance(b, str):
            result = str(a) + str(b)
        else:
            result = "Unsupported data types for addition"
    return result

# Testing the function
a = 3
b = 'Data'
print(add_variables(a, b))  

a = True
b = 5
print(add_variables(a, b)) 

a = 4.2
b = 7.8
print(add_variables(a, b)) 

a = 3 + 4j
b = 'Complex'
print(add_variables(a, b))  
