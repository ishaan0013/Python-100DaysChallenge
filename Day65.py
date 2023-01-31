#Static methods
class num:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        c=self.a+self.b
        return c
    @staticmethod
    def sub(a,b):
        return a-b
    
num1=num(10,20)
print(num1.addition())
print(num.sub(100,50))
print(num1.sub(20,10))