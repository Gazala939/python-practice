a = 100
b = 200
c = a+b
d = a*b
s1 ="a"
s2 = "b"
s3 = s1+s2
s4 = s1*3
print(c);print(d);print(s3);print(s4)

class Book():
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return (f"Total Pages: {self.pages}")

book1 = Book(100)
book2 = Book(200)

book3 = book1 + book2

print(book3)