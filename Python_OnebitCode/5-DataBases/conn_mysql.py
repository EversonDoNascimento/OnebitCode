import pymysql

connection = pymysql.connect(database= 'fliperama',
                             user='root', 
                             password='1234', 
                             host='localhost', 
                             port= 3306)


print("Conexão bem sucedida!")

