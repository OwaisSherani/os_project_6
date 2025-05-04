# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Static method to add two numbers
addition = MathUtils.add(5, 3)  # Calling the static method
print(f"The sum is: {addition}") 