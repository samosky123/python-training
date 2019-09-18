import re

output = '''
{
      "ROW_intf": {
        "intf-name": "Vlan100",
        "prefix": "192.168.22.251/24",
        "mask": "255.255.255.0",
        "ip-disabled": "FALSE",
        "iod": 2,
        "proto-state": "up",
        "link-state": "up",
        "admin-state": "up"
      }
'''

print("Example of matching exact string")
p = re.compile('192.168.22.251')
response = p.search(output)
if response:
    print(response.group(), response.span())

print("Example using re.match")
re_string = '192.168.22.251'
print("Regex string: {0}".format(re_string))
p = re.compile(re_string)
response = p.match(output)
if response:
    print(response.group(), response.span())

print("Example of matching substring and returning an iterator")
re_string = '\d*\.\d*\.\d*\.\d*'
print("Regex string: {0}".format(re_string))
response = re.finditer('\d*\.\d*\.\d*\.\d*', output)
if response:
    for item in response:
        print(item.group(), item.span())

print("Example of matching all substrings and returning them in a list")
re_string = '\d*\.\d*\.\d*\.\d*'
print("Regex string: {0}".format(re_string))
response = re.findall(re_string, output)
print(response)

print("Example of alternative expression for IP address and IP address with prefix")
re_string = '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/?[0-9]{1,2}'
print("Regex string: {0}".format(re_string))
response = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/?[0-9]{1,2}', output)
print(response)

print("Example of string replacement with Regex")
re_string = '\d*\.\d*\.\d*\.\d*'
print("Regex string: {0}".format(re_string))
p = re.compile(re_string)
print(p.subn('192.168.22.251', output, count=0))

# Exercise:
# 1. Split string into lines
# 2. Loop through the list of lines and print lines, which contain IP addresses in it


