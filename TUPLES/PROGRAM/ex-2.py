word = input("Enter the string:")
sd = set(word)
vowels = ('aeiouAEIOU')
result = sd.intersection(vowels)
print("The set with differnce vowels are =",result)


