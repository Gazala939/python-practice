def linearSearch(array,n,x):
    for i in range(0,n):
        if array[i] == x:
            return i
    return -1
array = [2,4,0,1,9,7,11,5,100,4]
x = 100
n = len(array)
resultant_position = linearSearch(array,n,x)

if resultant_position == -1:
    print("The given searching object is not found in the array.")
else:
    print(f"The given searching object is identifies in an array at index {resultant_position}")