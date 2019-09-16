# Ex.3
#

# Strings are enclosed in quotes (single or double)

switch1 = 'core_sw_01'

print('I have configured', switch1)

another_switch = 'core_sw_02'

print('WARNING: Switches', switch1, 'and', another_switch, 'configured.')

# Concatenate (join) strings with +

msg = 'WARNING: Switches ' + switch1 + ' and ' + another_switch + ' configured.'
print(msg)

"""
The string "ukdc1-asw01" has eleven characters,
numbered 0 to 10, as shown below:

+---+---+---+---+---+---+---+---+---+---+---+
| u | k | d | c | 1 | - | a | s | w | 0 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10

Part of a string is called a slice.

"""

name = 'ukdc1-asw01'
first_letter = name[0]
last_letter = name[10]
last_letter = name[-1]
prefix = name[0:9]

len(name)    # Returns length of variable name (function works on other data types)
name.lower() # Returns lowercase copy of name (string method)
name.upper() # Returns uppercase copy of name (string method)

# Get last two characters of switch name
switch_number = name[-2:]

# Convert to integer
switch_idx = int(switch_number)

# Add 1 
next_switch_idx = switch_idx + 1

# Convert back to string
next_switch_number = str(next_switch_idx)

# Add on leading '0'
next_switch_number = '0' + next_switch_number

# Construct next_switch_name string

next_switch_name = prefix + next_switch_number

