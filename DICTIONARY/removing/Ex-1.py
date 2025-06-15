fruits = eval(input("Enter the record of the fruits:"))
print(type(fruits))
fruits["kiwi"]=250
fruits["Jackfruits"]=125
fruits["Banana"]=500
print(type(fruits))
print(id(fruits))
print(fruits)

del fruits['apple']
print(fruits)

fruits.pop('Banana')
print(fruits)

data = fruits.popitem()
print(data)
print(fruits)