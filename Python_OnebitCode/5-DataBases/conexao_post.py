import psycopg2 

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = '1234',
    host = '127.0.0.1',
    port = 5432
)


print("Conexão bem sucedida!")

