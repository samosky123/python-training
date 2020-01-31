#!/usr/bin/env python
# Script connects to Arista switch via API, collects output of 'show ver' and prints
# OS version
import requests
import urllib3
import json
import getpass
import sys
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)
urllib3.disable_warnings(urllib3.exceptions.SNIMissingWarning)

DEBUG = True

def main():
    #device = 'evo-nxos01'
    #username = 'admin'
    #password = 'admin'
    device = input('Device hostname or IP address: ')
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    if device and username and password:
        authdata = (username, password)
        headers = {'Content-Type': 'application/json-rpc'}

        try:
            # Create requests session
            device_session = requests.Session()
            # Set HTTP payload
            data = [
                    {
                        "jsonrpc": "2.0",
                        "method": "cli",
                        "params": {
                                "version": 1,
                                "cmd": "show version",
                                },
                        "id": 1
                    }
            ]
            # Set HTTP URL
            url_command = 'http://{0}/ins'.format(device)
            # POST
            response = device_session.post(url_command, data=json.dumps(data), headers=headers, auth=authdata)
            # Close session
            device_session.close()
            # Check HTTP response code
            if response.status_code == 200:
                output = response.json()
                if DEBUG:
                    pprint(output)
                nxos = output['result']['body']['kickstart_ver_str']
                print('Software version:', nxos)
            else:
                # Print the code if it is not 200
                print(f'ERROR: HTTP Status code {response.status_code}')
        # Something's gone wrong
        except Exception as e:
            # Print error message
            print(f'ERROR: Connection failed {str(e)}')
    else:
        # If any of the arguments are empty or null
        print('No device, username or password provided')
        sys.exit(1)

if __name__ == '__main__':
    main()