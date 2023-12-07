'''

    Class Product and method discount
    Development a class in python to meet the following
    specificities of a product:

    1 - For each product must has a method of discount

    2 - The class must has a method construct and the dundle str

    3 - The class must has a method for discount.
    The method must receiver the discount in percentage and realize
    the calc how much would it cost the final price with the discount

'''

class Product:
    def __init__ (self, name, price):
        self.name = name
        self.price = price
        self.product_with_discount = 0.0
    
    def __str__(self) -> str:
        print(f"The name of product is: {self.name}\n" 
              f"The original price of the product is: ${self.price}\n"
              f"The product with discount cost: ${self.product_with_discount}")

    def discount(self,percentage):
        self.product_with_discount = self.price - self.price * percentage 
    
tv = Product("TV", 1000.0)
tv.discount(0.90)
tv.__str__()