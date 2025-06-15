str = "Hello"
for char in str:
    print(char)

print(iter("Python"))
print(iter([1,2,3,4,5,6,7]))
print(iter({}))

# How to handle the exception while using the iteratior:

d = iter(("abc","def","ghi","jkl","lmn"))
print(next(d))

while True:
    try:
        n = next(d)
        print(n)
    except StopIteration:
        break

