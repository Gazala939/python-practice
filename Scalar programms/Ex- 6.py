# Read input
A = int(input())

# Check if the number is prime
if A == 1:
    print("NO")  # 1 is not a prime number
elif A == 2:
    print("YES")  # 2 is a prime number
else:
    is_prime = True
    for i in range(2, A):
        if A % i == 0:
            is_prime = False
            break

    if is_prime:
        print("YES")  # A is prime
    else:
        print("NO")  # A is not prime

A = int(input())

if A == 1:
    print("NO")

elif A == 2:
    print("Yes")

else:
    is_prime = True
    for i in range(2, A):
        if A % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Yes")
    else:
        print("No")