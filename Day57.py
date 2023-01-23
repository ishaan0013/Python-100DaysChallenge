#OOPs concept- classes and objects

class Person:
    name=""
    age=0
    occupation=""
    def info(self):
        print(f'{self.name} is a {self.occupation} of age {self.age}.')
#This is a class
        
    
a=Person()
a.name='Ishaan'
a.occupation="Student"
a.age=22
#These are the objects of that class
a.info()
