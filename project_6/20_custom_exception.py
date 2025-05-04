# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. 
# Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self,age, message = "Age must be at least 18."):
        self.age = age
        self.message = message
        super().__init__(self.message)
# check age function
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print("Age is valid")

try:
 user_age = int(input("Enter your age: "))
 check_age(user_age)
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e.message}")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")