import sqlite3

connection = sqlite3.connect("./title.db")

cursor = connection.cursor()


data = cursor.execute("""
               SELECT * FROM movies
               ORDER BY score DESC
               """)

# Apresentando todos os dados da tabela
#print(data.fetchall())

for movie in data:
    print(movie)



connection.close()