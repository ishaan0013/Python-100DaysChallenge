#Instance variables vs Class variables

class Employee:
    def __init__(self,name):
        self.name=name
        # This is an instance variable
    def info(self):
        print(f"{self.name} is working in {self.company} and it's raise is {self.raisee}")
    noOfEmployee=0
    company="Apple"
    noOfEmployee+=1
    raisee=0.50
    # All 4 above are class variable
    
emp1=Employee("Ishaan")
emp1.company="Google"
emp1.info()
Employee.info(emp1)
# Both above 2 statement are same
        
        