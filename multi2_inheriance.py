#This is our second demonstration of multiple inheritance
# We will be having 3 Parent classes
# We will have 2 examples


#Case Chores
#Base Class 1
class House:

    #constructor
    def __init__(self, grocery, electronics, toiletry, furniture):
        self.grocery = grocery
        self.toiletry = toiletry
        self.electronics = electronics
        self.furniture = furniture

    #method 1: grocery
    def getGrocery(self):
        groc = input("Enter the grocery to buy: ", )
        self.grocery = groc
        return self.grocery
    
    #method 2: electronics
    def getElectronics(self):
        electronic = input("Enter the electronic to buy: ", )
        self.electronics = electronic
        return self.electronics
    
    #method 3: furniture
    def getFurniture(self):
        furnit = input("Enter the furniture being bought: ", )
        self.furniture = furnit
        return self.furniture
    
    #method 4: Toiletry
    def getToiletry(self):
        toilet = input("Enter the toiletry being bought: ", )
        self.toiletry = toilet
        return self.toiletry
    
#Base Class 2 : Kitchen Chores
class Kitchen:

    #Constructor
    def __init__(self, perishable, drygrain):
        self.perish = perishable
        self.dry = drygrain

    #method 1: Arrangement (if statement)
    def Arrange(self):
        perish = 25
        dry = 45
        item = input("Enter the item: ", )
        item_2 = input("Enter the item: ", )
        

        #If statement
        if(item <= perish):
           self.perish = print("Store in The Fridge")
        elif(item_2 <= dry and item_2 != perish):
            self.dry = print("Store in the cabinet")
        else:
            print("Store it in the grocery basket")
        
        return (self.dry or self.perish)
        

#Base class 3
class LivingRoom:

    #constructor
    def __init__(self, entApp, DinePl):
        self.dine = DinePl
        self.ent = entApp

    #Method 1: Where we wipe
    def DoWipe(self):
        dine = 1
        dust = 1
        

        #if statement
        if(dine == 1):
            self.dine = print("You need to wipe it")
        elif(dust == 1):
            self.ent = print("You have to dust off the appliances")
        else:
            print("The living room is clean")
        return (self.dine or self.ent)

#Derived class
class Activity(House, Kitchen, LivingRoom):

    #define the constructor
    def __init__(self):
        House.__init__(self, " "," ", " ", " " )
        Kitchen.__init__(self, " ", " ")
        LivingRoom.__init__(self, 0, 0)

    #method 1
    def shopped_items(self):
        print(self.grocery)
        print(self.toiletry)
        print(self.electronics)
        print(self.furniture)

    #method 2
    def arrangement(self):
        print(self.dry)
        print(self.perish)

    #method 3
    def activityDone(self):
        print(self.dine)
        print(self.ent)

# Creating object
action_1 = Activity()

#Call onto methods
print(action_1.activityDone())
    

    