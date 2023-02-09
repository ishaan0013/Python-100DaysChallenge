#dir, __dict__ and help method
list1=[1,2,4,'Ishaan',False]
print(dir(list1))

class Person:
    def __init__(self,name):
        self.name=name

a=Person("Ishaan")
print(a.__dict__)

print(help(Person))
        