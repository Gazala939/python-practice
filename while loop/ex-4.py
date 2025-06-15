# count the number

number = int(input("Enter the number:"))
num = number
count = 0

while num > 0:
    num = num // 10
    count += 1

print(f"The {number} of digit is : {count}")