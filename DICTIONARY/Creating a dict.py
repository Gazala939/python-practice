# Creating a Dictionary

person = {
    'name' : 'Gazala',
    'age' : 25,
    'city' : 'Gulbarga'
}
print(person['name'])
print(person['age'])
print(person['city'])

# Modifying dict.

person['age'] = 24
print(person['age'])

# Adding items to dict
person['state'] = 'Karnataka'
print(f"The person state is :{person['state']}")
print(person)

# Removing using del and pop method

del person['age']
print(person)

state = person.pop('state')
print(state)
print(person)

# length of dict

print(len(person))

# only keys:
print(person.keys())
print(person.values())
print(person.items())

print(person.values())







