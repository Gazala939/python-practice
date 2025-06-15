class accessModifier():
    a = 100
    b = "python"      # public data

    __c = 12.11
    __d = True

    _e = 1122
    _d = 0b11001

am = accessModifier()

print("The public data:")
print(am.a)
print(am.b)

print("the private data:")
print(am._accessModifier__c)
print(am._accessModifier__d)

print("The protected Data:")
print(am._e)
print(am._d)