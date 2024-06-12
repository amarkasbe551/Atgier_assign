# 8. WAP for user defined exceptions.

class number():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def div(self):
        return self.num1 // self.num2

number1 = number(10,0)
try:
    print(number1.div())
except ZeroDivisionError:
    print("Second Number Can't Be Negative")


# try:
#     example_function()
# except CustomError as e:
#     print("Custom error caught:", e)
