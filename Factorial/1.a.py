num = int(input("Enter the number:"))
factorial = 1

if num < 0:
    print("factorial does not exist for negative number:" )
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")