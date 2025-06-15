class Employee():
    def __init__(self,name = 'user',pos = None,salary = None):
        self.ename = name
        self.epos = pos
        self.esalary = salary

    def printData(self):
        print("The employee detail are:")
        print("Name of the employee =",self.ename)
        print("Position of the employee =",self.epos)
        print("Salary of the employee=",self.esalary)

emp = Employee()
emp1 = Employee("Gazala","developer",45000)
emp2 = Employee("Gazzo","Frontend",54000)
emp3 = Employee("Gj","engeneer",22000)


emp.printData()
print()
emp1.printData()
print()
emp2.printData()
print()
emp3.printData()