# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Show from Class A")
class B(A):
    def show(self):
        print("Show from Class B")
class C(A):
    def show(self):
        print("Show from Class C")
class D(B, C):
    pass

# Create an object of class D
d = D()
 # now call the show() method
d.show()

#print the method resulotion order
print(D.__mro__)
