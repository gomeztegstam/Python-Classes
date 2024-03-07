class AnimalShelter:
    def __init__(self):
        self.anidict = {}

    def addAnimal(self, animal):
        if self.anidict.get(animal.species) == None:
            self.anidict[animal.species] = [animal]
        else:
            self.anidict[animal.species].append(animal)

    def removeAnimal(self, animal):
        if animal.species in self.anidict:
            for i, a in enumerate(self.anidict[animal.species]):
                if a.species == animal.species and a.name == animal.name and a.age == animal.age and a.weight == animal.weight:
                    self.anidict[animal.species].pop(i)

    def removeSpecies(self, species):
        species = species.upper()
        if species in self.anidict:
            self.anidict.pop(species)

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        anilist = ''

        if species in self.anidict:
            for animal in self.anidict[species]:
                anilist += animal.toString()
                anilist += '\n'
            anilist = anilist[:-1]

        return anilist

    def doesAnimalExist(self, animal):
        if animal.species in self.anidict:
            for i in self.anidict[animal.species]:
                if i.species == animal.species and i.name == animal.name and i.age == animal.age and i.weight == animal.weight:
                    return True

        return False
