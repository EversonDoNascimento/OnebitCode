class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show(self):
        print(f"Name {self.name} - Salary {self.__salary}")

   

employee1 = Employee("Everson", 4000)
employee1.show()
employee1.__salary = 1000
employee1.show()
