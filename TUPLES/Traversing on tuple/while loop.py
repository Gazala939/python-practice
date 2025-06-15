my_tuple = ("python")
length = len(my_tuple)
print(length)

index = 0
while index < length:
    print(f"The element at positive index {index} and the element at negative index {index-length} is = {my_tuple[index]}")
    index +=1
print()

i =-1
while i > -length:
    print(f"The element at negative index {i} and the element at positive index {i+length} is = {my_tuple[i]}")
    i -= 1
