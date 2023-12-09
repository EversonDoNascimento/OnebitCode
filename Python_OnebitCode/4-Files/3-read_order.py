
class Student:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str):
            raise TypeError("Not is a string")
        else:
            self._name = name

class Student_list:
    def __init__(self):
        self.list = []
    
    def add_student(self, student):
        with open("data/names.txt", 'a', encoding= 'utf-8') as file:
            file.write(f"{student.name}\n")

    def sort_list(self):
        self.list = []
        with open("data/names.txt", 'r', encoding="utf-8") as file:
            for line in file:
                self.list.append(f"{line.strip()}")
        with open("data/names.txt", 'w', encoding='utf-8') as file:
            self.list.sort()
            for student in self.list:
                file.write(f"{student}\n")

    def show_students(self):
        self.sort_list()
        if len(self.list) == 0:
            print("Não há alunos na lista! Adicione algum aluno.")
        else:
            with open("data/names.txt", 'r', encoding="utf-8") as file:
                print("All students:\n")
                for line in file:
                    print(f"{line.strip()}")
    
    def remove_students(self, name):
        
        self.sort_list()
        if len(self.list) == 0:
            print("Não há alunos na lista para remover")
        
        else:
            for i,student in enumerate(self.list):
                if name == student:
                    self.list.pop(i)
                    print(f"Removendo {name}")
                    print("Estudante removido com sucesso!")
                    
        with open('data/names.txt', 'w', encoding='utf-8') as file:
            for student in self.list:
                file.write(f"{student}\n")
       
student_list = Student_list()

done = False

while not done:
    print("Escolha uma opção:")
    print("1 - Adicionar estudante")
    print("2 - Listar estudantes")
    print("3 - Remover estudante")
    print("4 - Sair")

    choice = int(input("Digite a opção que escolheu: "))

    if choice == 1:
        name_student = input("Digite o nome do estudante: ")
        student = Student(name_student)
        student_list.add_student(student)
        print("Estudante cadastrado com sucesso!")
        
    elif choice == 2:
        print("-"*40)
        student_list.show_students()
        print("-"*40)

    elif choice == 3:
        name_remove = input("Digite o nome do estudante que deseja remover: ")
        student_list.remove_students(name_remove)
        
    elif choice == 4:
        done = True
        print("Finalizando lista de alunos...")

    else:
        print("Opção inválida")