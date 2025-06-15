# WAP in python to element duplicate elements present in the list

ld = [1,2,3,4,5,6,2,3,4,5]
print("The orignel list is = ",ld)
sd = set(ld)
print("The set from the list=",sd)
ld = list(sd)
print("The list without duplicate is =",ld)