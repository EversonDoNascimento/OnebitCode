class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
    
    def __str__(self):
        return f"{self._brand} {self._model_name}"
    
    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")
    
class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera
    
Moto = Phone("Moto", "G", 900)
print(Moto)
Moto.make_a_call(394039409)    
print(f"Valor do {Moto._brand} {Moto._model_name} é {Moto._price}")
print(vars(Moto))

Iphone = Smartphone("Iphone", "13", 6000, "4GB", "256GB", "128MP")
print(Iphone)
Iphone.make_a_call(3384349384)
print(f"O Smartphone {Iphone._brand} {Iphone._model_name} custa {Iphone._price}")
print(vars(Iphone))