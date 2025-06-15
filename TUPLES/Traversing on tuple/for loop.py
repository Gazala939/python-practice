td = (1,2,3,4,5,6)
length = len(td)
print(td)
index=0
for i in td:
    print(f"The element at positive index {index} and the element at negative index {index-length} is = {td[index]}")
    index+=1

index = -1
for i in td:
    print(f"The element at negative index {index} and the element at positive index {index+length} is = {td[index]}")
    index-=1