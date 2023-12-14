import sqlite3


# 1 - Conectando no BD
connection = sqlite3.connect('title.db')

# 2 - Criando um cursor

'''

Cursor é um interador que permite navegar e manipular
os registros em um BD

'''

cursor = connection.cursor()

# 3 - Inserindo dados
'''
cursor.execute("""
            
           INSERT INTO movies (name, year, score) 
            VALUES ('Casablanca', 1942, 8.5);
               """)

connection.commit()
'''

print("Dado inserido com sucesso!")

connection.close()

