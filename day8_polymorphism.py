class Bird:
    def fly(self):
        print("Birds can fly")

class Penquin(Bird):
    def fly(self):
        print("Penquins cant fly , They swim")

# Using polymorphism 
        

def flying_test(x):
    x.fly()

sparrow = Bird()
penquin = Penquin()

flying_test(sparrow)
flying_test(penquin)