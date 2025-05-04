class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} \nAge: {self.age}")

studen1 = Student("Owais", 30)
studen1.display()