class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def show(self):
        print(f"Name {self.name} - Salary {self.__salary}")

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        self.__salary = salary

employee1 = Employee("Everson", 4000)
employee1.show()
employee1.__salary = 1000
employee1.show()
employee1.set_salary(1000)
print(employee1.get_salary())