import requests
import json

ip = 'evo-eos01'

authdata = {'username': 'admin', 'password': 'admin' }
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url_login = 'https://{0}/login'.format(ip)
url_logout = 'https://{0}/logout'.format(ip)

device_session = requests.Session()

response = device_session.post(url_login, data=json.dumps(authdata), headers=headers, verify=False)
if response.status_code == 200:

    data = {
                "jsonrpc": "2.0",
                "method": "runCmds",
                "params": {
                           "version": 1,
                           "cmds": [ "show version" ],
                           "format": "json"
                          },
                "id": "1"
               }

    url_command = 'https://{0}/command-api'.format(ip)

    response = device_session.post(url_command, data=json.dumps(data), headers=headers, verify=False)
    if response.status_code == 200:
        output = response.text
        print(output)

    response = device_session.post(url_logout, data=json.dumps(authdata), headers=headers, verify=False)

    if response.status_code == 200:
        for line in response.text.split('\n'):
            if 'Software image' in line:
                print('Version:', line.split(':')[1])
    
    else:
        print(f'ERROR: HTTP Status code {response.status_code}')
    
    device_session.close()