def fun(a,b):
    sum = a + b
    print(sum)
fun(3,2)

# WAP to creat the fdunction to check whether the given three sides from the right angle triangle or not

def checkTriangle(a,b,c):
    if(a**2 + b**2 == c**2)or(b**2 + c**2 == a**2)or(a**2 + c**2 == b**2):
        print("It is a right angle trianle ")
    else:
        print("It is not a right angle triangle.")

checkTriangle(7,8,9)
checkTriangle(5,5,5)
checkTriangle(3,4,5)

