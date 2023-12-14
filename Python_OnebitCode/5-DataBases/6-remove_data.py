import sqlite3

connection = sqlite3.connect("./title.db")

cursor = connection.cursor()

id = int(input("Infome o id do filme que deseja remover: "))

cursor.execute("""
               DELETE FROM movies
               WHERE id = ?;
               """, (id,))

connection.commit()
print("Deletado com sucesso!!")

connection.close()