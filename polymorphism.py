#The existence of an object in many forms
# we will have 2 examples
#the examples will be of shapes

#Case study 1: Circle
#Base class
class circle:

    #constructor
    def __init__(self):
        self.pi = 3.142
        self.radius = 0

    #method: get radius
    def Radius(self):
        radius = int(input("Kindly enter the Radius value: ", ))
        self.radius = radius
        print("The radius is: ", self.radius)

#Form 1: Cylindar pi r2h
class cylindar(circle):

    #Form
    def render(self):

        height = int(input("Enter the height: ", ))
        vol = self.pi * self.radius * self.radius * height
        print("The volume is: ", vol)

#Form 2: Sphere SA = 4/3PIR3
class sphere(circle):

    #method
    def render(self):    
        surface = 4/3 * self.radius *self.radius *self.radius * self.pi
        print("The Surface area is: ", surface)

#Create objects
sphere1 = sphere()
cylindar1 = cylindar()

#Methods
print(sphere1.Radius())
print(sphere1.render())
