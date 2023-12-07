class Animal:
    def __init__(self,name, category):
        self.name = name
        self.category = category

class Fish(Animal):
   pass

class Parrots(Animal):
    pass

class Zoo:
    def __init__(self):
        self.animals_dict = {}
    
    def add_animal(self, animal):
        self.animals_dict[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.animals_dict.values():
            if animal == category:
                result += 1
        return f"No nosso zoológico temos {result} quantidade de {category}"

zoo = Zoo()
fish = Fish("Nemo", "mamíferos")
print(vars(fish))
parrots = Parrots("Louro", "aves")
print(vars(parrots))
zoo.add_animal(fish)
zoo.add_animal(parrots)
print(zoo.total_of_category("aves"))