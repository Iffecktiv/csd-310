from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.icskrbr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())
