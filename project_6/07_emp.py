# Create a class Employee with: a public variable name, a protected variable _salary, and a private variable __ssn. Try 
# accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

# Create an object
emp = Employee("Owais", 50000, "123-45-6789")

print("Name:", emp.name)  # Accessing public variable
print("Salary:", emp._salary)  # Accessing protected variable (not recommended, but possible)

try:
    print("SSN:", emp.__ssn)  # ❌ Will raise an AttributeError
except AttributeError as e:
    print("Error:", e)

print("SSN (via name mangling):",emp._Employee__ssn) # Works, but should be avoided outside class definition