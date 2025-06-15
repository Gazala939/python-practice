class accessModifier():
    a = 123
    __b = 121
    _c = 1122
    
    def printData(self):
        print("The public data is =",self.a)
        print("The private data is =",self.__b)
        print("The protected data is =",self._c)

am = accessModifier()
am.printData()