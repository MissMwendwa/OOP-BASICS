# This is the second example
# the case study we'll use will be for Company protocol

# Ecommerce company
#abstract class
class Complaint:

    #const
    def __init__(self):
        self.name = " "
        self.sku_no = 0
        self.complaint = " "

    #method 1: get compain
    def complain(self):
        #statements
        pass

    #method 2: get info
    def info(self):
        #statements
        pass

    #method 3: submit
    def submit(self):
        #statememts
        pass


#client 1
class Client_1(Complaint):

    #const
    def __init__(self):
        self.name = " "
        self.complain = " "
        self.sku_no = 0

    #method 1
    def comp1(self):
        complaint = input(" Enter the client concerns: ", )
        self.complain = complaint
        print("The clients issue is: ", self.complain)

    #method 2
    def info1(self):
        NClient = input("Enter the client name: ", )
        sku_no = int(input("Enter the SKU_No. : ", ))
        self.sku_no = sku_no
        self.name = NClient
        print("Client name: ", self.name)
        print("SKU Number: ", self.sku_no)

    #method 3
    def status(self):

        status = input("Is the issue resolved: ", ).lower()
        
        #Decision tree
        if(status == "yes"):
            print("The complaint has been resolved successfully!")
        else:
            print("The complaint needs attention")

#Object
Mark = Client_1()

#Methods
print(Mark.comp1())
print(Mark.info1())
print(Mark.status())
