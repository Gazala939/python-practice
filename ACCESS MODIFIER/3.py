class accessModifier():
    a = 123
    __b = 121
    _c = 23

    def printData(self):
        print("The public data:",self.a)
        print("The private data:",self.__b)
        print("The protected data:",self._c)

    def publicData(self):
        self.p = "Python"
        self.q = True

    def privateData(self):
        self.__x = 1234

    def protectedData(self):
        self._y = 4321

    def checkData(self):
        print("The public data:", self.p,self.q)
        print("The private data:",self.__x)
        print("The protected data:",self._y)

    def methodParameter(self,r,s,t):
        return r+s+t

    @staticmethod
    def static():
        accessModifier.__d2 = 112

    def instance(self):
        print("The static method data =",accessModifier.__d2)


am = accessModifier()
am.printData()
am.publicData()
am.privateData()
am.protectedData()
am.checkData()
d1 = 121
__d2 = 122
_d3 = 23

print(am.methodParameter(d1,__d2,_d3))
accessModifier.static()
am.instance()



