from conexao_post import connection

cursor = connection.cursor()

cursor.execute("""
               
               SELECT * FROM fliperama.games
               
               """)

cursor.execute()