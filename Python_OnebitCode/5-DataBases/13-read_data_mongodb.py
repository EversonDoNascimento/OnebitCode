from pymongo import MongoClient
from pprint import pprint
client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts
temp = ""
for post in mycol.find():
    if "Java" in post.values():
        temp = post
  

pprint(temp)



