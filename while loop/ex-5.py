# find the sum of individual digit of a number 1234

number = 1234
num = number
sum_of_digit = 0

while num > 0:
    digit = num % 10
    sum_of_digit += digit
    num = num// 10
print(f"The sum of {number} is:{sum_of_digit}")