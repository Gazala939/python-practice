class Person():         # Class definition (use uppercase for class names)
    name = "Gazala"        # Class attribute
    age = 24                  # Class attribute
    gender = "Female"         # Class attribute

# Creating an instance (object) of the class
user1 = Person()

# Accessing class attributes using the object
print(user1.name)
print(user1.age)
print(user1.gender)

user2 = Person()
user2.name = "ABC"
user2.age = 23
user2.gender = "female"
print(user2.name)
print(user2.age)
print(user2.gender)