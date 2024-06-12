# 2.  Write a Python class named Student with two attributes student_id, student_name.
# Add a new attribute student_class and display the entire attribute and their values of the said class.
# Now remove the student_name attribute and display the entire attribute with values.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Attributes and their values:")
        print(f"Student ID: {self.student_id}")
        if hasattr(self, 'student_name'):
            print(f"Student Name: {self.student_name}")
        if hasattr(self, 'student_class'):
            print(f"Student Class: {self.student_class}")

    def remove_attribute(self, attribute_name):
        delattr(self, attribute_name)


# Creating an instance of the Student class
student1 = Student(1, "Alice")

# Displaying attributes and their values
student1.display_attributes()

# Adding a new attribute
student1.student_class = "Class 10"

# Displaying attributes and their values after adding student_class
print("\nAfter adding student_class attribute:")
student1.display_attributes()

# Removing student_name attribute
student1.remove_attribute("student_name")

# Displaying attributes and their values after removing student_name
print("\nAfter removing student_name attribute:")
student1.display_attributes()

