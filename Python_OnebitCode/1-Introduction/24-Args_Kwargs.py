# 1 - Use *Args for receiver a quantity of arguments undefined = Data receiver equal Tuple

# 2 - Use **Kwargs for receiver a quantity of arguments undefined = Data receiver equal Dictionary

def sum(*num):
    temp = 0
    for i in num:
         temp += i
    return temp

print(sum(2,4,4,5,6,3,1))


def apresentation(**data):
     for key, value in data.items():
          print(f"{key} : {value}")

courses = {
     
}

apresentation(name = "JS",carga_horária = "26 horas", instrutor = "Everson Nascimento")