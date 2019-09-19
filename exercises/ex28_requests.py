import requests
from pprint import pprint as pp

with requests.get('http://standards-oui.ieee.org/oui.txt') as response:
    print('Response HTTP Code:', response.status_code)

output = response.text

oui_dict = {}

for line in output.split('\r\n'):
    if '(base 16)' in line:
        oui = line.split('(base 16)')[0].strip()
        company = line.split('(base 16)')[1].strip()
        oui_dict[oui] = company

pp(oui_dict)

# Example:
# gw = '0010db'.upper()
#
# oui_dict[gw]
# 
