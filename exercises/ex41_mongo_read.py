import datetime
from pymongo import MongoClient
client = MongoClient('0.0.0.0:27017')
db = client.pystud16

for doc in db.inventory.find():
    idx = doc["_id"]
    db.inventory.update({"_id": idx}, {"$set":{"updated": datetime.datetime.now()}})
    print("Inventory item ", doc["name"], "updated.")

