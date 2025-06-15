n = 10

for row in range(1,n+1):
    for col in range(1, row+1):
        print(col,end = " ")
    print()

for row in range(5,1,-1):
    for col in range(1,row):
        print("* ",end = " ")
    print()

for row in range(1,n+1):
    for col in range(1,row+1):
        print("* ",end = " ")
    print()