class Animal:
    def __init__(self, species = None, weight=None, age = None, name = None):
        if type (species) == str:
            self.species = species.upper()
        else:
            self.species = None
        self.weight = weight
        self.age = age
        if type (name) == str:
            self.name = name.upper()
        else:
            self.name = None

    def setSpecies(self, species):
        self.species = species.upper() 

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper() 

    def toString(self):
        return f'Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight}'
