#This is the second example of polymorphism
#It will be an animal example

#Origin class
class animal:

    #Constructor
    def __init__(self):
        self.movement = " "
        self.sound = " "
        self.name = " "

#Form 1 : Cat
class Cat(animal):

    #method: name 
    def getName(self):
        name = input("Enter the Cat name: ", )
        self.name = name
        return self.name

#Form 2 : Dog
class Dog(animal):

    #Method : Name
    def getName_2(self):
        name_2 = input("Enter the dog name: ", )
        self.name = name_2
        return self.name
    
#Form 3: Parrot
class Parrot(animal):

    #Method :  Name
    def getName_3(self):
        name_3 = input("Enter the parrot name: ", )
        self.name = name_3
        return self.name
    

#Object Creation
cat = Cat()
dog = Dog()
parrot = Parrot()

#Call method
print(cat.getName())
print(dog.getName_2())
print(parrot.getName_3())