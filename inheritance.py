# We will be demonstrating inheritance in 3 cases
# We will be using the constructors in the examples
# syntax

'''class base_class:
    properties

class derived_class(base+_class):
    methods'''


#Case study 1: Person
#below is the base class
class Person:

    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #method 1
    def getName(self):
        return self.name
    
    #method 2
    def getAge(self):
        return self.age
    

#Derived Class 1: Education
class Education(Person):

    #method: Educated
    def isEducated(self):
        return True
    
#Objects created
person_1 = Person("Hailey", 23)
person_1 = Education("Hailey", 23)

#print statements
#print(person_1.isEducated())
#print(person_1.getAge())



#Case 2: Electric Shop
#This is the base class
class Electric_shop:

    #constructor
    def __init__(self,pd_name, quantity, price):
        self.name = pd_name
        self.quantity = quantity
        self.price = price

    
#Derived class Holds methods
class Methods(Electric_shop):

    #method 1
    def getName(self):
        return self.name
    
    #method 2
    def getQuantity(self):
        Quantity = int(input("Please input the quantity: ", ))
        self.quantity = Quantity
        return self.quantity

    #method 3
    def getPrice(self):
        cost = int(input("Enter the cost: ", ))
        self.price = self.quantity * cost
        return self.price
    
#object Methods
Laptop = Methods("Hellewett Pack", 0, 0)
#print(Laptop.getQuantity())
#price
#print(Laptop.getPrice())

#In all the examples we have done so far are just about Single Inheritance

#Case with super() keyword
#Base class
class Electric_shop:

    #constructor
    def __init__(self,pd_name, quantity, price):
        self.name = pd_name
        self.quantity = quantity
        self.price = price

#Derived class 1(Has been converted into a super class using Super() keyword to also allow inheritance)
class name(Electric_shop):

    #Create a new constructor
    def __init__(self, pd_name, quantity, price):
        self.sname = pd_name
        self.squantity = quantity
        self.sprice = price

    #method
    def getname(self):
        name = input("Enter the device name: ", )
        self.name = name
        return self.name
    
# Inherit from name
class Laptop(name):

    def getPrice(self):
        price = int(input("Enter the price: ", ))
        self.sprice = price
        return self.sprice
    
#Creating an object
lappy = Laptop(" ", 0, 0)

#print out price
print(lappy.getPrice())
print(lappy.getname())
