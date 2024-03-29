#Multiple Inheritance 

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"My name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name

obj = DancerEmployee("Ishaan", "Pop")
print(obj.name)
print(obj.dance)
obj.show() 
# print(DancerEmployee.mro())