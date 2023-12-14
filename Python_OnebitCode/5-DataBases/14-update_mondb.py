from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

result = mycol.update_one({"title": "Ruby"},{"$set":{ "content": "Ruby is very good", "category": "Programation"}})
