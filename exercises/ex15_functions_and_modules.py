# Ex. 15

# We will refactor this code into functions in ex16

s1 = { 'name': 'fra2-a10', 'type': 'N9K-C9372PX-E', 'version': 'n9000-12.0(1q)' }
s2 = { 'name': 'chc1-a01', 'type': 'N9K-C9372PX-E', 'version': 'n9000-12.0(1q)' }
s3 = { 'name': 'chc1-a02', 'type': 'N9K-C93128TX', 'version': 'n9000-12.0(1q)' }

switches = [s1, s2, s3]

#print switches

for switch in switches:
    print 'Name:', switch['name']
    print 'Type:', switch['type']
    print 'Version:', switch['version']
    print '+------------------------------------------------------------+'
