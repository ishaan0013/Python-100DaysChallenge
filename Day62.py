#access modifiers
#In Python, we don't actually have Private,Protected,Public 
#but we can actually use it indirectly

class Student:
    def __init__(self,name):
        self.__name=name
    
a=Student("Ishaan")
# print(a.__name)
#the above line will through error
#So we can use it in different ways
#Like

print(a._Student__name)
       
    