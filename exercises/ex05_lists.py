# Ex.5
#

# Python list is a collection of values.

empty_list = []

interfaces = ['Eth1', 'e2', 7, 1.1]

vlans = [100, 101, 102, 103]

for vlan in vlans:
    print 'VLAN:', vlan
    # end of the code block
print "Number of VLANs", len(vlans)

print 'Second VLAN in list is', vlans[1]
print 'Last VLAN in list is', vlans[-1]

# Start with a string
out = 'MTU 1500 bytes, sub MTU 1500, BW  149760 Kbit, DLY 80 usec,'
# split into list of strings
words = out.split(' ')

mtu = words[1]
sub_mtu = words[5]
bw = words[8]
dly = words[11]

print mtu, sub_mtu, bw, dly

# exercise
# Print again with bw divided by 2 and dly multiplied by 2