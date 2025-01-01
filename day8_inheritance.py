# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def features(self):
        print(f"{self.name} has 4 legs")

    def speak(self):
        print("This animal makes sound")

# Child Classes
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def speak(self):
        #super().speak()  # Call parent class's speak
        print(f"{self.name} says: Meow!")


#instances of child class
        
dog1 = Dog("Buddy")
cat1 = Cat("Whiskers")

dog1.speak()
cat1.speak()
dog1.features()
cat1.features()