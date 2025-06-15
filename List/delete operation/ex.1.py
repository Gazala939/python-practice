ld = eval(input("Enter the number:"))
print("Before deleting list:",ld)
del ld[3]
print("After deleting the list:",ld)
ld.clear()
print(ld)