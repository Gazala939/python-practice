# Reverse the order

number = 12345
reverse = 0
n = number

while n!=0:
    ind_dig = n % 10
    reverse = reverse*10 + ind_dig
    n = n//10
print(f"the reverse order of {number} is:",reverse)





