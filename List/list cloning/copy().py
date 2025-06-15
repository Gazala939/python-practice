x = [1,2,3,4,5,6]
y = x.copy()
print(id(x))
print(id(y))
print(x)
print(y)
x[0]= 0
print(x);print(id(x))
y[5] = 7
print(y);print(id(y))