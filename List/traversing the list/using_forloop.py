lstdata = [1,2,3,4,5,6]
length = len(lstdata)
index = 0
for ele in lstdata:
    print(f"The element at positive index {index} and the element at negative index {index-length} is = {ele}")
    index +=1
index=-1
for ele in lstdata[::-1]:
    print(f"The element at negative index {index} and  at positive index {index+length} is = {ele}")
    index -=1