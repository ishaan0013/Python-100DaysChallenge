#Single Inheritance
class Fruit:
    def __init__(self,name):
        self.name=name
    def info(self):
        print(f'This is a {self.name}')
        
class Apple(Fruit):
    pass

kashmiri_apple=Apple("Kashmiri apple")
kashmiri_apple.info()
