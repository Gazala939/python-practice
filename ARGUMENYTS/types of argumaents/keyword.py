# WAP to creste the function to calculate the simple intreset

def simpleIntereset(principle,time,rate):
    SI = (principle*time*rate)/100
    total_amount = principle*SI
    print("The total amount=",total_amount)

p = int(input("Enter the number:"))
r = int(input("Enter the number:"))
t = int(input("Enter the number:"))
simpleIntereset(rate = r,principle=p,time=t)