import random

# 1 - Selecionando um valor da lista
list = [2,3,4,1,2,6,4,1,2,5,7]
print(random.choice(list))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

# 3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list, 2))
print(random.sample(list,5))
s = "Hello World"
print(random.sample(s,3))
