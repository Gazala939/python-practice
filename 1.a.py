# Quadratic equation
# ax2 + bx + c
# x = -b+-squarroot of b2-4ac/2a

import math
a = float(input("Enter the coffient of a:"))
b = float(input("Enter the coeffient of b:"))
c = float(input("Enter the coeffient of c:"))

d = b**2 - 4*a*c

if d > 0:
    root1 = (-b + math.sqrt(d))/2*a
    root2 = (-b - math.sqrt(d))/2*a
    print("Two real root" ,root1, "and", root2)
elif d == 0:
    root = -b / (2* a)
    print("One real root:",root)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d)/ (2*a)
    print("Two complex roots:", f"{real}+{imag}i and {real}-{imag}i")

