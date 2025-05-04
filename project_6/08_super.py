# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, 
# and use super() to call the base class constructor.

# Base class Person
class Person:
    def __init__(self, name):
        self.name = name # Constructor to set the name
        print(f"Person constructor called for {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call the base class constructor
        self.subject = subject
        print(f"Teacher constructor called for {self.name}, Subject: {self.subject}")

t1 = Teacher("Owais", "Python")  # Creating an object of Teacher class
    
