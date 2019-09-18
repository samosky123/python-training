import datetime
import pymongo
import requests
import json
import pprint

switch_name = 'nexus01'

url='http://129.213.66.127/ins'

switchuser='admin'

switchpassword='admin'

mongo_client = pymongo.MongoClient()

db = mongo_client.pystud14

myheaders={'content-type':'application/json-rpc'}

payload=[

  {

    "jsonrpc": "2.0",

    "method": "cli",

    "params": {

      "cmd": "show interface status",

      "version": 1.2

    },

    "id": 1

  }

]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

data = response['result']['body']['TABLE_interface']['ROW_interface']

for interface in data:
    interface_name = interface['interface']
    state = interface['state']
    duplex = interface['duplex']
    speed = interface['speed']

    result = db.interfaces.insert({'switch': switch_name, 'interface_name': interface_name,
                                   'state': state, 'duplex': duplex, 'speed': speed, 'updated': datetime.datetime.now()})

    print('Result:', result)
