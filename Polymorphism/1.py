class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __mul__(self,other):
        return self.salary * other.days

class timesheet():
    def __init__(self,name,days):
        self.name = name
        self.days = days

e = Employee("Gazala",4500)
t = timesheet("Gazala",25)

print("The arjun salary of the september month :", e*t)
