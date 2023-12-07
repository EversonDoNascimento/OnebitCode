'''
1 - the class method uses the parameter referring to the class 
2 - The class method can access or modify the state of class
3 - We use the decorator @classmethod to create a new class method
'''
class Console:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    

xboxOne = Console.from_text("Meu video game é XboxOne e o preço é 1000 reais")

# Transformando em dicionario

print(xboxOne.__dict__)