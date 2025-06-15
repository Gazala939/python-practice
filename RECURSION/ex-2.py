def reverseString(string):
    reverse = " "
    for i in string:
        reverse = i+reverse
    return reverse

data = input("Enter the name:")
print("The reverse of string = ",reverseString(data))