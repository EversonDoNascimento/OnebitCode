import requests
from pymongo import MongoClient

# 1 - Estabelecendo conexão com o mongo e criando DB

client = MongoClient()

db = client["nobel"]

# 2 - Importar os dados em documentos

for colletion_name in ["prizes", "laureates"]:
    response = requests.get( f"https://api.nobelprize.org/v1/{colletion_name[:-1]}.json")
    document = response.json()[colletion_name]
    #print(document)
    db[colletion_name].insert_many(document)

# Contagem de documents    
prizes = db['prizes'].count_documents({})
laureates = db['laureates'].count_documents({})

print(prizes)
print(laureates)