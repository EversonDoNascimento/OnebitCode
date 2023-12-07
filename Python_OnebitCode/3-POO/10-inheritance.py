class Animal:
    __name = ""
    __size = ""
    __color = ""
  
    
    def comer(self):
        print(f"O animal está comendo")


class Horse(Animal):
    race = ""
    
    def scape(self):
      print("Cavalo fugindo")

class Lion(Animal):
    mane = True

    def hunt(self):
        print("Leão caçando")
    
h = Horse()
h.__name = "Carpeado"
h.__color = "Preto"
h.__size = "2 metros"
h.comer()

l = Lion()
l.__name = "Lion"
l.__color = "Amarelo"
l.__size = "3 metros"
print(l.__name)
l.comer()
l.hunt()