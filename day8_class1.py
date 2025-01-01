import math
class Circle:

    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * math.pi
    def circumference(self):
        return 2 * math.pi * self.radius
    
circ1 = Circle(9)
print("Area: ", circ1.area())
print("Circumference: ", circ1.circumference())
