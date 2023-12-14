import sqlite3

# 1 - Criando o BD

connection = sqlite3.connect("title.db")


# 2 - Verifica se houve alterações ma base de dados
print(connection.total_changes)