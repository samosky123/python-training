# Ex. 9
#

arp_table = [{'mac': '0080:2101:cd07', 'ip': '10.10.197.8', 'age': '22'},
             {'mac': '005e:97b2:0854', 'ip': '10.10.197.4', 'age': '119'},
             {'mac': '0081:2778:a9b9', 'ip': '10.10.197.7', 'age': '37'},
            ]


search = '005e:97b2:0854'
for entry in arp_table:
    if entry['mac'] == search:
        print('IP:', entry['ip'], 'MAC:', entry['mac'])


# arp_table as dictionary of dictionaries
#

arp_table = {'0080:2101:cd07': {'ip': '10.10.197.8', 'age': '22'},
             '005e:97b2:0854': {'ip': '10.10.197.4', 'age': '119'},
             '0081:2778:a9b9': {'ip': '10.10.197.7', 'age': '37'}
            }

search = '005e:97b2:0854'
print('IP:', arp_table[search]['ip'], 'MAC:', search)

for mac in arp_table:
    print('IP:', arp_table[mac]['ip'], 'MAC:', mac)


# exercise
#
# Create MAC table as dictionary as dictionary
#
# mac             port          vlan   age
# 0080:2101:cd07  Eth1/1        2200   55
# 005e:97b2:0854  Eth1/7        2200   0
# 0081:2778:a9b9  Eth1/19       2200   171
