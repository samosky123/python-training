# Ex. 8
#

s1 = ['fra2-a10', 'N9K-C9372PX-E', 'n9000-12.0(1q)']
s2 = ['chc1-a01', 'N9K-C9372PX-E', 'n9000-12.0(1q)']
s3 = ['chc1-a02', 'N9K-C93128TX', 'n9000-12.0(1q)']

switches = [s1, s2, s3]

print(switches)

for switch in switches:
    print('Name:', switch[0])
    print('Type:', switch[1])
    print('Version:', switch[2])
    print('+------------------------------------------------------------+')

# Using a dictionary

s1 = { 'name': 'fra2-a10', 'type': 'N9K-C9372PX-E', 'version': 'n9000-12.0(1q)' }
s2 = { 'name': 'chc1-a01', 'type': 'N9K-C9372PX-E', 'version': 'n9000-12.0(1q)' }
s3 = { 'name': 'chc1-a02', 'type': 'N9K-C93128TX', 'version': 'n9000-12.0(1q)' }

switches = [s1, s2, s3]

#print switches

for switch in switches:
    print('Name:', switch['name'])
    print('Type:', switch['type'])
    print('Version:', switch['version'])
    print('+------------------------------------------------------------+')


# List of dictionaries is very common structure

# exercise
#
# Create ARP table (list of dictionaries) with three entries:
#
# mac             ip          age
# 0080:2101:cd07  10.10.197.8 22
# 005e:97b2:0854  10.10.197.4 119
# 0081:2778:a9b9  10.10.197.7 37

