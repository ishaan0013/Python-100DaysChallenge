#Class Methods
class Employee:
    company='Apple'
    def __init__(self,name) -> None:
        self.name=name
    def info(self):
        print(f'{self.name} is in  company-{self.company}')
    @classmethod
    def changeCompany(cls,cmp):
        cls.company=cmp

emp1=Employee('Ishaan')
emp1.info()
Employee.company="google"
emp1.info()