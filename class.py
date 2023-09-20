# This will be our first OOP attempt
# We will explore use of classes in Python
# We'll have simple class demos'

#Syntax
'''class class_name:
    statements
    OR 
    def func():
        statements


create class_obj
call on class_obj'''

#Create a class holding human attributes
class human:

    #Features
    feature_1 = "legs"
    feuture_2 = "eyes"
    feature_3 = "Breasts"
    feature_4 = "dimples"

#Creating an object
anne = human()
#print(anne.feature_1)


#Create Class Chicken
class Chicken:

    #Chicken Features
    feat_1 = "Feathers"
    feat_2 = "Thighs"
    feat_3 = "wings"
    feat_4 = "beak"

    #Chicken activities
    act_1 = "lay eggs"
    act_2 = "crow"
    act_3 = "sleep"

#Create a chicken object
chick = Chicken()

#call our obj
#print(chick.act_2)


#Class Car 

class car:

    #Car parts
    part_1 = "dashboard"
    part_2 = "wheels"
    part_3 = "hood"
    part_4 = "bumper"
    part_5 = "brake shoe"
    part_6 = "Car engine"

    #Car models
    mod_1 = "audi"
    mod_2 = "benz"
    mod_3 = "volvo"
    mod_4 = "toyota"
    mod_5 = "Ford"
    mod_6 = "Porshe"
    mod_7 = "bentley"


#Object creation
car_mine = car()
print(car_mine.part_3)
print(car_mine.mod_4)


    


