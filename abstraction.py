# We will be drawing an abstract class for shapes
#Then we will use that information to build real classes

#Shape Example
#Abstract class
class Shape:

    #Const
    def __init__(self):
        self.name = " "
    
    #Method 1: Perimeter
    def perimeter(self):
        #statements
        pass

    #method 2: Area
    def area(self):
        #statements
        pass

    #method 3: print statement
    def fact(self):
        #statement
        pass


#Real classes
class circle(Shape):

    #Constructor
    def __init__(self):
        self.name = " "
        self.radius = 0

    #method 1
    def CPerimeter(self):
        radius = int(input("Enter the radius: ", ))
        self.radius = radius
        perimeter = 3.142 * (self.radius *2)
        print(perimeter)

    #method 2
    def CArea(self):
        radius = int(input("Enter the radius: ", ))
        self.radius = radius
        area = 3.142 * self.radius * self.radius
        print(area)

    #method 3
    def Fact(self):
        name = input("Enter the shape name: ", )
        self.name = name
        print("The shape is a ", self.name)

#hape 2: Rectangle
class Rectangle(Shape):

    #const
    def __init__(self):
        self.name = " "
        self.length = 0
        self.width = 0

    #method 
    def RPerimter(self):
        len = int(input("Enter the length: ", ))
        wid = int(input("Enter the width: ", ))
        self.length = len
        self.width = wid
        perimeter_r = 2 * (self.length + self.width)
        print(perimeter_r)

    #method 2
    def RArea(self):
        len = int(input("Enter the length: ", ))
        wid = int(input("Enter the width: ", ))
        self.length = len
        self.width = wid
        area_r = self.length * self.width
        print(area_r)

    #method 3
    def RFact(self):
        name_r = input("Enter the name of the shape: ", )
        self.name = name_r
        print("The name of the shape is ", self.name)

#Create objects
rect = Rectangle()
circ = circle()

#Call onto methods
#print(circ.Fact())
print(rect.RArea())
