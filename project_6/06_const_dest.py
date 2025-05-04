#Create a class Logger that prints a message when an object is created (constructor) and another message 
# when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created!")  # Constructor message

    def __del__(self):
        print("Logger object destroyed!")  # Destructor message

log = Logger()  # Creating an object of Logger class   
del log  # Deleting the object to trigger the destructor message