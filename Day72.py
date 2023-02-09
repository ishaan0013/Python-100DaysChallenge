#super keyword
class Employee:
    def __init__(self):
        print('This is 1st class')

class Person(Employee):
    def __init__(self):
        print('This is 2nd class')
        super().__init__()
        
a=Person()

