import math

# 1 - Acessar o número PI

print(f"{math.pi:.2f}")

# 2 - Acessar o número de Euler
print(f"{math.e:.2f}")

# 3 - Arredondando números para cima e baixo
num = 10.4
print(math.ceil(num))
print(math.floor(num))

# 4 - Fatorial de um número

num2 = int(input("Digite um número"))
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(2,3))

# 6 - Raiz quadrada
print(int(math.sqrt(121)))

# 7 - MDC 
mdc = math.gcd(25,100)
print(mdc)

# 8 - Logaritmo
print(math.log(10))