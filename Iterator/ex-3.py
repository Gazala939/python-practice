class myClass:
    def __init__(self,n):
        self.start = -1
        self.end = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end - 1: #As long as start < end - 1, it increases start by 2 and returns it.
            self.start +=2
            return self.start
        else:
            raise StopIteration
obj = myClass(5)

while True:
    try:
        t = next(obj)
        print(t)
    except StopIteration:
        break

"""Initial: start = -1, end = 5

Step	start Before	start += 2	Returned	start < end - 1
1	-1	1	1	True
2	1	3	3	True
3	3	5	--	False (5 < 4 = False) → raises StopIteration"""

