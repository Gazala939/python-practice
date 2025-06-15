lstdata = eval(input("Enter the list:"))
length = len(lstdata)
print("The length of lstdata is",length)

index=0
print("the positive index:")
while index < length:
    print(f"The element at positive index {index} and the element at negative index {index - length} is = {lstdata[index]}")
    index+=1


index = -1
print("The negative to positive indexing:")
while index > -length:
    print(f"The element at negative index {index} and the element in positive indexing {index + length} is = {lstdata[index]}")
    index-=1