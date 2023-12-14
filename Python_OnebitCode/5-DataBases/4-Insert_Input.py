import sqlite3


# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor

'''

Cursor é um interador que permite navegar e manipular
os registros em um BD

'''

cursor = connection.cursor()

# 3 - Solicitando dados

name = input("Digite o nome do filme: ")
year = int(input("Digite o ano de lançamento: "))
score = float(input("Digite a nota de avaliação: "))

# 4 - Inserindo dados



cursor.execute("""
        
        INSERT INTO movies (name,year,score) 
        VALUES (?, ?, ?)
            
               """, (name,year,score))


#Gravando dados no BD
connection.commit()

print("Dado inserido com sucesso!")

connection.close()

