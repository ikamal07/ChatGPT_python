class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError
        self.__name = name #private attribute
        self.__age = age

    #Getter Method
    def access(self):
        print("Name is", self.__name)
        print("Age is", self.__age)
    
    #Setter Method
    def update(self,name1):
        self.__age = self.__age + 10
        self.__name = name1
    

person1 = Person("Johny", -33)
person1.access()
person1.update("Vijay")
person1.access()

    
    