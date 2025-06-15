num = int(input("Enter the number:"))
orignal_num = num
reversed_num = 0
while num >= 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

    if orignal_num == reversed_num:

        print(f"{orignal_num} is palindrom")
    else:
        print(f"{orignal_num}is not a palindrom")