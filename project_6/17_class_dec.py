#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!".
# Apply it to a class Person.

# def class _decorator(cls):
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls
@add_greeting   
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Owais")
print(p.greet())  # Output: Hello from Decorator!
    

