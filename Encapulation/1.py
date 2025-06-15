class publicData():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printMethod(self):
        print("Name :",self.name)
        print("Age :",self.age)

    def __privateMethod(self):
        print("Name :",self.name)
        print("Age :",self.age)

    def _protectedMethod(self):
        self.__privateMethod()

pD = publicData("Gazala",24)
pD.printMethod()
pD._protectedMethod()