# WAP to display unique vowels present in the given number

words = input("Enter a word:")
vowels = "aeiouAEIOU"
result = list()

for l in words:
    if l in vowels:
        if l not in result:
            result.append(l)

print("A list with unique vowels=",result)
print("The number of unique vowels are",len(result))


