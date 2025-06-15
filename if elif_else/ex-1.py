#  percentage

s1 = int(input("Enter the marks:"))
s2 = int(input("Enter the marks:"))
s3 = int(input("Enter the marks:"))
s4 = int(input("Enter the marks:"))

total = s1+s2+s3+s4

percentage = total//4

if percentage > 85:
    grade = "A"

elif percentage >= 70  and percentage <= 85:
    grade = "B"

elif percentage >= 55 and percentage <= 70:
    grade = "C"

elif percentage >= 40 and percentage <= 55:
    grade = "D"

else:
    grade ="F"

print("The total number of marks of the student:",total)
print("The percentage of student:",percentage)
print("The grade of the student",grade)
