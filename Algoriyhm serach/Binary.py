def binarySearch(array,x,low,high):
    while low <= high:
        mid = low + (high-low)//2

        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid +1

        else:

            high = mid-1

    return -1

array = [2,4,5,7,6,3,8,9]
x = 8

resultant_position = binarySearch(array,x,0,len(array)-1)

if resultant_position == -1:
    print("Result is not found")
else:
    print("The result is found at the index", resultant_position)