# 1. Use of Class Objects and constructor in Python Program to create a class called ComplexNumber that consist of variables real and imag,
# functions like constructor and getData().
# Create  objects c1 and c2. add C1 and C2  and print the addition and also contents of c1 and c2

class ComplexNumber:

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def getData(self):
        print(f"Real part:-{self.real}")
        print(f"Imag part:-{self.imag}")
    
    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

# Creating objects c1 and c2
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

# Printing contents of c1 and c2
print("Contents of c1:")
c1.getData()
print("\nContents of c2:")
c2.getData()

# Adding c1 and c2
result = c1 + c2

# Printing the result
print("\nResult of addition:")
result.getData()
