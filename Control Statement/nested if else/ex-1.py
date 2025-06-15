#  Determine the Largest of Three Numbers

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter the third number:"))

if a>b:
    if a>c:
        print(f"The largest number is {a}")

    else:
        print(f"The largest number is {c}")

else:

    if b>c:
        print(f"The largest number is {b}")

    else:
        print(f"The largest number is {c}")