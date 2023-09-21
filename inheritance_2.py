# This is what we are doing
# We are creating a class that holds properties only
# Inherit the properties to create methods
# Create objects from the class

#Case study : Fruits
class Fruit:

    #properties
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

# Inherited class to hold the methods
class info(Fruit):

    #method 1: Name
    def getName(self):
        return self.name
    
    #method 2 : color
    def getColor(self):
        color = input("The color is: ", )
        self.color = color
        return self.color
    
    #method 3: price
    def TotalPrice(self):
        cost = int(input("Enter the price of one: ", ))
        num = int(input("Enter the total number of fruits bought: ", ))
        total = cost * num
        self.price = total
        return self.price
    
#Create an object
#banana = info("Banana", " ", 0)

#print(banana.TotalPrice())
#print(banana.getColor())

# We are hard-coding the methods
fruit_1 = Fruit(" ", " ", 0)

#start of hard-code methods
fruit_1_name = input("Enter the name: ")
fruit_1.name = fruit_1_name

print(fruit_1.name)