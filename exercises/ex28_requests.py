import requests
#Import pprint as pp
from pprint import pprint as pp

# Use context manager to open up HTTP GET request
with requests.get('http://standards-oui.ieee.org/oui.txt') as response:
    print('Response HTTP Code:', response.status_code)

# Decode response as Text
output = response.text

# Initialize dictionary named as oui_dict
oui_dict = {}

# Iterate through list of output lines (output split into list by end of line sequence)
for line in output.split('\r\n'):
    if '(base 16)' in line:
        oui = line.split('(base 16)')[0].strip()
        company = line.split('(base 16)')[1].strip()
        oui_dict[oui] = company

# Print resulted dictionary
pp(oui_dict)

# Example:
# gw = '0010db'.upper()
#
# oui_dict[gw]
# 
