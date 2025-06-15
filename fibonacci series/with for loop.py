nterms = int(input("Enter the number:"))

a,b = 0,1
count = 0

if nterms <= 0:
    print("Enter the positive integer:")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(a)
        c = a + b
        a = b
        b = c
        count+=1