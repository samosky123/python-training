import os
import sys

path = os.getcwd()

hostname = input('Enter hostname:')

if hostname.startswith('sw'):
    new_path = os.path.join(path, hostname)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
else:
    sys.exit('Hostname has to start with "sw"')
