#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method 
#that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, val):
        return val * self.factor
multi = Multiplier(5)

print(callable(multi))  # Output: True, because multi is callable

result = multi(10)
print(result)  # Output: 50, because 10 * 5 = 50

