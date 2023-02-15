#Multilevel Inheritance
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def info(self):
        Animal.info(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
        
    def info(self):
        Dog.info(self)
        print(f"Color: {self.color}")

obj= Dog("tommy", "Black")
obj.info()
print(GoldenRetriever.mro())
