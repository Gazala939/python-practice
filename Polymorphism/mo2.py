class Calculator():
    def sum(self,*n):
        total = 0

        for num in n:
            total += num
        return total

calci = Calculator()
calci.sum(100)
calci.sum(1,2,3,4,5,6)
print(calci.sum(100))
print(calci.sum(100,200,300))