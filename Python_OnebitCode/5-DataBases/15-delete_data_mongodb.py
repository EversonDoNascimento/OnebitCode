from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = {"title": "Ruby"}

result = mycol.delete_one(myquery)

# How many documents removed:
print(f"Quantity of documents removed: {result.deleted_count}")