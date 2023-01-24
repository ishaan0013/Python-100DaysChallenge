#Constructors

class Fruit:
    name=""
    colour=""
    pieces=0
    total_quantity=0
    def info(self):
        print(f'I have {self.pieces} {self.name} of {self.colour} colour.And total of {self.total_quantity}KG\'s')
        
apple=Fruit()
apple.name="Apple"
apple.colour="RED"
apple.pieces=10
apple.total_quantity=100
apple.info()
#this is the normal method but we can solve the problem of initialization by the help of Constructors
#Example:=

class Vehicle:
    def __init__(self,name,numbers,colour):
        self.name=name
        self.numbers=numbers
        self.colour=colour
    def info(self):
        print(f"I have {self.numbers} {self.name} of {self.colour} colour.")
        
Car=Vehicle("BMW",10,"White")
Car.info()
#here we are doing same thing but with the help of a Constructor

        
        

    