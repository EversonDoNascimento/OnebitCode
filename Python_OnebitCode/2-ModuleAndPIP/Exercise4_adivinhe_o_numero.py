import random

numero_aleatorio = random.randint(0,10)


condicao = False
tentativas = 0   
while not condicao:
    
    numero_escolhido = int(input("Digite um número de 0 a 10 para tentar adivinhar: "))
    if(numero_aleatorio == numero_escolhido):
        condicao = True
        print("Parabéns você acertou o número aleatório!!")
    else:
        tentativas += 1
        print("Tente novamente!!")
        print(f"Você já tentou {tentativas} vezes")