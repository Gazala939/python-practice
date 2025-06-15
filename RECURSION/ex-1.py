def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)  # multiply n with factorial(n-1)
# taking input from the user

num = int(input("Enter the number:"))

# checking for negative numbers

if num < 0:
    print("Factorial is not define for negative numbers")
else:
    print(f"Factorial of {num} is {factorial(num)}")
5