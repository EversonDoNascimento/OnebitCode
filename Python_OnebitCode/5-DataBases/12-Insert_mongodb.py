from pymongo import MongoClient

client = MongoClient()
# Criando o banco de dados
mydb = client.obcblog
# Criando Collection
mycol = mydb.posts

post1 = {
    "title": "Python",
    "category": "Automation",
    "content": "Python is very good!",
    "author": {
        "name": "Everson",
        "email": "everson@gmail.com"
    }
}

post2 = {
    "title": "Javascript",
    "category": "Development Web ",
    "content": "Web is very good",
    "author": {
        "name": "Everton",
        "email": "everton@gmail.com"
    }
}

post3 = {
    "title": "Java",
    "category": "Spring boot",
    "content": "Java is very good!",
    "author": {
        "name": "Gustavo",
        "email": "gustavo@gmail.com"
    }
}
mycol.insert_one(post2)
mycol.insert_one(post3)

print("Document insert with success!")