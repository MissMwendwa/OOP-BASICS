#This will be the demonstration of Multiple inheritance
# Here we will have parent classes and no super classes
# There will be 2 examples

#Case 1: shopping center/supermarket

#Base class 1
class Supermarket:

    #constructor
    def __init__(self, grocery, detergent, bakery):
        self.grocery = grocery
        self.bakery = bakery
        self.detergent = detergent
        
    #methods : 1
    def getGrocery(self):
        groc = input("Enter your grocery of choice: ", )
        self.grocery = groc
        return self.grocery
    
    #method 2
    def getDetergent(self):
        deter = input("Enter your detergent of choice: ", )
        self.detergent = deter
        return self.detergent
    
    #method 3
    def getBakery(self):
        bake = input("Enter the confectionary of choice: ", )
        self.bakery = bake
        return self.bakery
    
#Base class 2
class shop:

    #constructor
    def __init__(self, crockery, toiletry):
        self.crockery = crockery
        self.toiletry = toiletry
        

    #method 
    def getStuff1(self):
        toilet_s = input("Enter your toilet essential: ", )
        self.toiletry = toilet_s
        crock = input("Enter the crokery of choice: ", )
        self.crockery = crock
        return (self.toiletry + self.crockery) 
    
# Multiple inheritance
#Derived class
class shopping(Supermarket, shop):

    #due to the diff constructors we initialize both constructor here
    #we have created a new inherited construtctor from both parent classes
    def __init__(self):
        Supermarket.__init__(self, ' ', " ", " ")
        shop.__init__(self, " ", " ")

    #method
    def getList(self):
        print(self.bakery)
        print(self.grocery)
        print(self.detergent)
        print(self.toiletry)
        print(self.crockery)
      
  
# Create objects 
shopping = shopping() 

#Calling the methods
print(shopping.getBakery())
print(shopping.getDetergent())
print(shopping.getStuff1())
print(shopping.getList())
