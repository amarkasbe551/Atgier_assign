# 5. Write a Python class which has two methods  get_String and print_String.
# get_String accept a  string from the user and print_String print the  string in upper case.

class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_string(self):
        self.user_string = input("Enter a string: ")

    def print_string(self):
        print("String in uppercase:", self.user_string.upper())

string_manipulator = StringManipulator()
string_manipulator.get_string()
string_manipulator.print_string()




