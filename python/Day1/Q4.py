# A docstring in Python is a string literal that occurs as the first statement in a module, function, class, or method definition.


def add_numbers(x, y):
    """
    This function adds two numbers together.
    
    Parameters:
    x (int): The first number.
    y (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return x + y

# Accessing the docstring using __doc__ attribute
print(add_numbers.__doc__)

# R8esult
result = add_numbers(3, 5)
print("Result:", result)  

