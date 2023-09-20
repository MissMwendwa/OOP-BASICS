# We will be performing some class operations
# We shall use condtructors in this class
# It shall demonstrate the use of classes, objects, methods and constructors

#Case study 1: Person in a company

class Person:

    #constructor
    def __init__(self, name , age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    #method to get the name
    def getName(self):
        return self.name
    
    #method calculate age
    def getAge(self):
        new_age = self.age + 2
        #print(new_age)
        return new_age
    
    #method to return the id_numeber
    def getID(self):
        return self.id_number
    
#Create an object
new_person = Person("Michael Muchemi", 45, 45609876)
#new_person = Person() this is wrong depending on how you have defined your comstructor
#We are calling onto the object Methods
#print(new_person.getAge())
#print(new_person.getName())

#Case Study 2: Cars
class Cars:

    #constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color
        
    #method 1
    def getModel(self):
        return self.model
    
    #Method 2
    def getColor(self):
        return self.color
    
#Create our object
car_1 = Cars("Toyota", "Twilight grey")
car_2 = Cars("Audi", "white")
car_3 = Cars("Mazda", "Black")

#Calling the methods
#print(car_2.getModel())
#print(car_3.getColor())


#Case Study 3: Fruits
class Fruits:

    #Constructor
    def __init__(self, shape, color, sugar_level, price):
        self.shape = shape
        self.color = color
        self.sugar_level = sugar_level
        self.price = price

    #method 1: shape
    def getShape(self):
        return self.shape
    
    #method 2: color
    def getColor(self):
        return self.color
    
    #method 3: Calculate sugar level
    def getSugar(self):
        self.sugar_level = 0
        new_level = self.sugar_level + (234/40)
        return new_level
    
    #method 4: Calculate price
    def getPrice(self):
        self.price = 0
        no_of_pieces = self.price + 14
        cost = 15
        total_price = no_of_pieces * cost
        return total_price


#Create object
fruit = Fruits("Cresent", "yellow", 0, 0)
fruit_2 = Fruits("Circle", "Orange", 0, 0)
fruit_3 = Fruits("Oval", "Black", 0, 0)
fruit_4 = Fruits("Oval", "green", 0, 0)
fruit_5 = Fruits("Oval", "yellow", 0, 0)
fruit_6 = Fruits("cylindrical", "yellow", 0, 0)


#Calling our Methods
print(fruit_4.getSugar())
print(fruit_6.getPrice())
print(fruit_3.getShape())
print(fruit_5.getColor())