class Product:
    def __init__(self, price, brand, type):
        self._price = price
        self._brand = brand
        self._type = type
    
    def show_product(self):
        print(f"This product is: {self._type}\nThe brand is: {self._brand}\nThe price is: $ {self._price}")
    
    def discount(self):
        self._price_with_discount = self._price - self._price * 0.10 
    
    def show_discount(self):
        print(f"The product with discount cost: $ {self._price_with_discount}")
    
class Smartphone(Product):
    def __init__(self,price,brand,type,ram,memory):
        super().__init__(price,brand,type)
        self.ram = ram
        self.memory = memory
    def discount(self):
        self._price_with_discount = self._price - self._price * 0.15 

class TV(Product):
    def __init__(self,price,brand,type,screen,sound):
        super().__init__(price,brand,type)
        self.screen = screen
        self.sound = sound
    def discount(self):
        self._price_with_discount = self._price - self._price * 0.25 
produto = Product(200,"Amazon","Tablet")
iphone = Smartphone(9000,"Apple","Iphone","6GB", "512GB")
tv = TV(2000,"Panasonic","Smart Tv","55 polegadas", "7.1 sorround")

produto.show_product()
produto.discount()
produto.show_discount()
print("-"*30)
iphone.show_product()
iphone.discount()
iphone.show_discount()
print("-"*30)
tv.show_product()
tv.discount()
tv.show_discount()