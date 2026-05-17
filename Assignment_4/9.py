class Herbivore:
    def __init__(self, name):
        self.name = name;
    
    def animalType(self):
        print("Herbivore");

class Carnivore:
    def __init__(self, name):
        self.name = name;
    
    def animalType(self):
        print("Carnivore");

class Omnivore:
    def __init__(self, name):
        self.name = name;
    
    def animalType(self):
        print("Omnivore");

class Bear(Herbivore, Carnivore, Omnivore):
    pass

a1 = Bear("Bear");
a1.animalType();