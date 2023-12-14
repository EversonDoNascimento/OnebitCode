from conn_mysql import connection

cursor = connection.cursor()

cursor.execute("""
                      
              SELECT * FROM fliperama.games;

               """)


result = cursor.fetchall()
print(result)

connection.close()
