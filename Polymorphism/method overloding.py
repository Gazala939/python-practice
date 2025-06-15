class calculator():
    def sum(self,a = None,b = None,c = None):
        if a != None and b != None and c != None:
            print("The sum of three numbers =",a+b+c)
        elif a != None and b != None:
            print("The sum of two numbers =",a+b)

        elif a != None:
            print("The sum of one number is =",a)

        else:
            print("Kindly provide atlest one argument for proceeding")

cala  = calculator()
cala.sum(25,12,32)
cala.sum(23,24)
cala.sum(76)

