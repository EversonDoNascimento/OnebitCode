from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista

fruits = ["Banana", "Uva", "Banana", "Maçã", "Pêra", "Laranja", "Uva", "Maçã"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando tupla noemada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa23", 90, 8.0)
g2 = game("Hallo 4", 302, 10.0)
print(g1)
print(g2)

# 3 - Ordenando diciońarios
studants = {"Pedro": 23, "Hanna": 29, "Gustavo": 20}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20,12,35,34])
deq.appendleft(44)
deq.append(90)
print(deq)
deq.pop()
deq.popleft()
print(deq)