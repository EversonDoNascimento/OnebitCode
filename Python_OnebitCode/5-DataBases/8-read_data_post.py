from conexao_post import conn

cursor = conn.cursor()

cursor = conn.cursor()

cursor.execute("SELECT * FROM game")

result = cursor.fetchall()

for game in result:
    print(game)

conn.close()
