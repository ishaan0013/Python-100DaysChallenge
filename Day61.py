#Inheritance

class Employee:
    def __init__(self,salary,name,id):
        self.salary=salary
        self.name=name
        self.id=id
class Manager(Employee):
    print("This is a very good employee")
    def info(self):
        print(f"Salary-{self.salary}, Name-{self.name}, Id-{self.id}")

a=Manager(1000,"Ishaan",3546)
a.info()