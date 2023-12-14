import sqlite3

connection = sqlite3.connect("./title.db")

cursor = connection.cursor()



# Solicitando dados do User

id = int(input("Informe o id do filme: "))
name= input("Digite o novo nome do filme")

# Atualizando dados

cursor.execute("""
               
            UPDATE movies
            SET name = ?
            WHERE id = ?   
               """, (name, id))


connection.commit()
print("Dados atualizado com sucesso")

connection.close()