#Encapsulation --> Data hiding
#We will be defining Public and Private members in Code
# Unlike other prog lang, python uses symbols instead of word representation in Public and Private declaration
# Private = single underscore(_) or Double underscore(__)

#First example(pricing case study)
class price:

    #Constructor
    def __init__(self):
        self._price1 = 400

    #method 1
    def sellPrice(self):
        sellPrice = self._price1 * (120/100)
        print("The selling price is: ", sellPrice)

    #method 2
    '''def getProfit(self):
        profit = sellPrice - self.price1
        print("The profit is: ", profit)'''
    

#Create object
MarkedP = price()

#Call the method
#print(MarkedP.sellPrice())


#Example 2: Derived Class
#Example Salaried employee
#Base class
class Person:

    #Constructor
    def __init__(self):
        self._name = " "
        self._salary = 0
        self._status = " "


    #Create method
    def getName(self):
        name = input("Enter your name: ", )
        self._name = name
        print("Employee Name: ", self._name)

    #method 2: salary
    def getSalary(self):
        sal = int(input("Enter the salary amount: ", ))
        self._salary = sal
        print("Salary due: ", self._salary)

    #method 3: emp status
    def Status(self):
        stat = input("Enter Emp status: ", )
        self._status = stat
        print("Employment Status: ", self._status)

#Derived class
class NewSalary(Person):

    #method : Calculate new salary
    def newSalary(self):
        sal_new = self._salary * (115/100)
        print("New Salary: ", sal_new)


#Create object
Alice = Person()
Alice = NewSalary()

#Call on methods
print(Alice.getSalary())
print(Alice.newSalary())

