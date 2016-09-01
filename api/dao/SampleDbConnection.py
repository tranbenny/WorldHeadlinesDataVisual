# connect to local mongodb instance

from pymongo import MongoClient

try:
    client = MongoClient("mongodb://localhost:8000")
except:
    print('error connecting to mongodb')

# accessing a database
db = client.test

# accessing a database's collection
collection = db.dataset

# add a sample document to sample collection
result = collection.insert_one(
    {
        "title": "sampleTitle",
        "value": "3"
    }
)

cursor = collection.find()
for document in cursor:
    print(document)
