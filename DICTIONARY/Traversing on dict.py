record = dict()
n = int(input("Enter the count for the record:"))
i = 1
while i <= n:
     name = input("Enter the name of the student:")
     percentage = input("Enter the percentage marks of the student:")
     record[name] = percentage
     i+=1
print("The student data in the given record is :")
for item in record:
     print("\t",item,"\t\t",record[item])











