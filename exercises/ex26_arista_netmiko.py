#!/usr/bin/env python
# Script connects to Arista switch via SSH, collects output of 'show ver' and prints
# OS version
from netmiko.arista import AristaSSH
import getpass
import sys
from pprint import pprint

DEBUG = True

def main():
    device = input('Device hostname or IP address: ')
    username = input('Username: ')
    password = getpass.getpass('Password: ')

    if device and username and password:
        try:
            # Connect to device cli shell
            device_shell = AristaSSH(device, username=username, password=password)
            # Find prompt
            prompt = device_shell.find_prompt()
            # Disable paging
            device_shell.disable_paging()
            # Send command and wait for prompt
            output = device_shell.send_command_expect('show ver', expect_string=prompt)
            # Disconnect
            device_shell.disconnect()
            if DEBUG:
                pprint(output)
            # Split output into list of lines
            output_line_list = output.split('\n')
            # For each line of output...
            for line in output_line_list:
                # If line contains 'Software image' text...
                if 'Software image' in line:
                    # Split line at ':' character, and keep everything after ':'
                    eos = line.split(':')[1].strip()
                    print('Software version:', eos)
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
