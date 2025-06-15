a = {1,2,3,4,5,6,7,8,}
b = {6,7,8,9}
c = a.union(b)       # UNION
print(c)

d = a.intersection(b)   # INTERSECTION
print(d)

e = a.difference(b)
print(e)
e1 = b.difference(a)
print(e1)

f = a.symmetric_difference(b)
print(f)