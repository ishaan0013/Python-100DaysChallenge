class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string1):
        return cls(string1.split("-")[0], int(string1.split("-")[1]))
    
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)
