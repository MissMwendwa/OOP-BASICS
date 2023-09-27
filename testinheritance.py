#ChatGPT code
#Case Chores
# Base Class 1
class House:

    #constructor
    def _init_(self):
        self.grocery = ""
        self.toiletry = ""
        self.electronics = ""
        self.furniture = ""

    #method 1: grocery
    def getGrocery(self):
        self.grocery = input("Enter the grocery to buy: ")
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
    def _init_(self):
        self.perishable = ""
        self.drygrain = ""

    #method 1: Arrangement (if statement)
    def Arrange(self):
        
        item = int(input("Enter the perishable item: "))
        item_2 = int(input("Enter the dry grain item: "))

        if item <= 25:
            self.perishable = "Store in The Fridge"
        elif item_2 <= 45:
            self.drygrain = "Store in the cabinet"
        else:
            return "Store it in the grocery basket"

        return self.drygrain or self.perishable
        

# Base Class 3 (LivingRoom)
class LivingRoom:
    def _init_(self, entApp="", DinePl=""):
        self.dine = DinePl
        self.ent = entApp

    def DoWipe(self):
        dine = 1
        dust = 1

        if dine == 1:
            self.dine = "You need to wipe it"
        elif dust == 1:
            self.ent = "You have to dust off the appliances"
        else:
            return "The living room is clean"

        return self.dine or self.ent or "The living room is clean"


#Derived class
class Activity(House, Kitchen, LivingRoom):

    #define the constructor
    def _init_(self):
        House._init_(self)
        Kitchen._init_(self)
        LivingRoom._init_(self)

    #method 1
    def shopped_items(self):
        print(self.grocery)
        print(self.toiletry)
        print(self.electronics)
        print(self.furniture)

    #method 2
    def arrangement(self):
        print(self.Arrange())  # Use the Arrange method from Kitchen class

    #method 3
    def activityDone(self):
        print(self.DoWipe())

# Creating object
action_1 = Activity()

# #Call onto methods
# print(action_1.activityDone())
# Call methods
action_1.shopped_items()
action_1.arrangement()
action_1.activityDone()