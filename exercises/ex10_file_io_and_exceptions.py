# Ex.10
#
# Use pycharm to run these samples

# Write to a file
data_out = ["mac             port          vlan   age",
            "0080:2101:cd07  Eth1/1        2200   55" ]


file = open("mac_table.txt", "w")
for line in data_out:
    file.write(line)
    file.write('\n')
file.close()

# Read a file
file = open("mac_table.txt", "r")
for line in file:
    print line

# New style
with open('mac_table.txt') as file:
    for line in file:
        print line

# What if file does not exist?
try:
    with open('mic_table.txt') as file:
        print file.readlines()
except:
    print "Error opening file"

# Read filename from keyboard
filename = raw_input('Filename:')
with open(filename) as file:
    text_lines = file.readlines()
    for text in text_lines:
        print text

# exercise
# Use try/except to deal with no such file errors
