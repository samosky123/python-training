# Ex.4
#

# String formatting with %
mtu = '1500'
sub_mtu = '1500'
bw = '149760'
dly = '80'

print 'MTU %s bytes, sub MTU %s, BW  %s Kbit, DLY %s usec,' % (mtu, sub_mtu, bw, dly)

# String formatting with .format

print 'MTU {0} bytes, sub MTU {1}, BW  {2} Kbit, DLY {3} usec,'.format(mtu, sub_mtu, bw, dly)

# Split function

out = 'MTU 1500 bytes, sub MTU 1500, BW  149760 Kbit, DLY 80 usec,'
words = out.split(' ')
phrases = out.split(',')

# exercise
# What is the data type of 'words' and 'phrases'?