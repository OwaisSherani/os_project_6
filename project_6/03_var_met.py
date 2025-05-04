# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable

    def start(self):  # Public method
        print(f"{self.brand} is starting...")

my_car = Car("Toyota")

print(my_car.brand)  # Accessing the public variable
my_car.start()  # Calling the public method