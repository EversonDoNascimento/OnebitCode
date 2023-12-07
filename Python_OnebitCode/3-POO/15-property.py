class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Não é uma string")
        else:
            self._name = value
        
person = Person("Everson",49)
print(vars(person))