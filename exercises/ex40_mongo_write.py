import datetime
from pymongo import MongoClient
client = MongoClient('0.0.0.0:27017')
db = client.pystud16

db.inventory.insert({"name": "ukdc1-sw01", "ip": "10.1.1.1/24"})
db.inventory.insert({"name": "ukdc1-sw02", "ip": "10.1.1.2/24"})
db.inventory.insert({"name": "ukdc1-sw03", "ip": "10.1.1.3/24"})
db.inventory.insert({"name": "ukdc1-sw04", "ip": "10.1.1.4/24"})


