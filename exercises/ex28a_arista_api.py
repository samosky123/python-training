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

DEBUG = False

def main():
    device = input('Device hostname or IP address: ')
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    if device and username and password:
        authdata = {'username': username, 'password': password }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        url_login = 'https://{0}/login'.format(device)

        try:
            # Create requests session
            device_session = requests.Session()
            # POST authentication data to login
            response = device_session.post(url_login, data=json.dumps(authdata), headers=headers, verify=False)
            # Set HTTPS payload
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
            # Set HTTPS URL
            url_command = 'https://{0}/command-api'.format(device)
            # POST
            response = device_session.post(url_command, data=json.dumps(data), headers=headers, verify=False)
            # Close session
            device_session.close()
            # Check HTTP response code
            if response.status_code == 200:
                output = response.json()
                if DEBUG:
                    pprint(output)
                eos = output['result'][0]['version']
                print('Software version:', eos)
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