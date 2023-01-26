#Getter & Setter

class Answer:
    def __init__(self,a,b):
        self.first=a
        self.second=b
        
    def info(self):
        print(self.first,self.second)
        
    @property
    def addition(self):
        return self.first+self.second
    
    @addition.setter
    def addition(self,newvalue):
        self.first=newvalue-self.second
        
obj=Answer(1,2)
obj.info()
obj.addition=10
obj.info()
        
        