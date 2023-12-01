import json

# 1 - Strings para Dicionários
person = '{"name":"Everson", "languagens":["Python","JS"]}'
person_dict = json.loads(person)
print(person_dict['languagens'])

# 2 - Convertendo Dicionários para json
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))

# 3 - Formatando json
print(json.dumps(person_dict, indent = 4, sort_keys = True))

# 4 - Salvando json em txt
with open("person.txt", "w") as json_file:
    json.dump(person_dict, json_file)

# 5 - Lendo arquivo txt
with open("person.txt","r") as file:
    conteudo = file.read()

print(conteudo)

# 6 - Lendo arquivo json externo
with open("teste.json","r") as person:
    content = json.load(person)
    print(content)