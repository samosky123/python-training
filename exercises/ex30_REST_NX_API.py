"""

 NX-API-BOT 

"""

import requests

import json

url='http://10.106.1.65/ins'

switchuser='admin'

switchpassword='admin'


myheaders={'content-type':'application/json-rpc'}

payload=[

  {

    "jsonrpc": "2.0",

    "method": "cli",

    "params": {

      "cmd": "show version",

      "version": 1.2

    },

    "id": 1

  }

]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

software_version = response['result']['body']['sys_ver_str']

print("Software Version:", software_version)

