# Ex.10
#
# Use pycharm to run these samples

# Write to a file
data_out = ["mac             port          vlan   age",
            "0080:2101:cd07  Eth1/1        2200   55" ]


f = open("mac_table.txt", "w")
for line in data_out:
    f.write(line)
    f.write('\n')
f.close()

# Read a file
f = open("mac_table.txt", "r")
for line in f:
    print(line)

# New style
with open('mac_table.txt') as f:
    for line in f:
        print(line)

# What if file does not exist?
try:
    with open('mic_table.txt') as f:
        print(f.readlines()
except:
    print "Error opening file"

# Read filename from keyboard
filename = raw_input('Filename:')
with open(filename) as f:
    text_lines = f.readlines()
    for text in text_lines:
        print text

# exercise
# Use try/except to deal with no such file errors
