# Create a class Engine and a class Car. Use composition by passing an Engine object to 
# the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start (self):
        print ("Engine is starting...")
# Car class using composition

class Car:
    def __init__(self, engine):
        self.engine  = engine  # Composition: Car has an Engine

    def start_car(self):
        print("The car is starting...")
        self.engine.start()  # Accessing the Engine's method

engine = Engine()  # Creating an Engine object
my_car = Car(engine)  # Creating a Car object with the Engine object
my_car.start_car()  # Starting the car, which will also start the engine
