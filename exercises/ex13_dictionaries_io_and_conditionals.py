# Ex. 13
#

# Read interface stats line by line.
# interface_stats is dictionary of dictionary
#
# interface_stats = {'Ethernet2/1': {'state': 'up', 'in_pkts': '0'}
#                        KEY      :   VALUE = dictionary
#
# interface_stats['Ethernet1/1'] = {'in_bcst_pkts': '303',
#                                   'in_pkts': '314',
#                                   'out_bcst_pkts': '0',
#                                   'state': 'up'}
#

interface_stats = {}
rx = True

with open('show_interface_small.txt', 'r') as f:
    for line in f:

        if line.startswith('Ethernet'):
            interface_name = line.split(' ')[0]
            #print 'Interface Name:', interface_name
            interface_stats[interface_name] = {}

        elif line.startswith('admin state'):
            state = line.split(' ')[3].split(',')[0]
            interface_stats[interface_name]['state'] = state

        elif line.startswith('  RX'):
            rx = True

        elif line.startswith('  TX'):
            rx = False

        elif line.find('input packets') > 0:
            pkts = line.split(' ')[4]
            interface_stats[interface_name]['in_pkts'] = pkts

        elif line.find('broadcast packets') > 0:
            pkts = line.split(' ')[12]
            if rx:
                interface_stats[interface_name]['in_bcst_pkts'] = pkts
            else:
                interface_stats[interface_name]['out_bcst_pkts'] = pkts

#print interface_stats

for interface,stats in interface_stats.iteritems():
    print(interface, 'STATE:', stats['state'], 'IN_PKTS:', stats['in_pkts'])
