# Ex.6
#

# More work with lists

switches = ['fra2-a10', 'fra2-a11', 'chc1-a01', 'chc1-a02']

# For each switch in the list'85
for switch in switches:
    # Split on '-' and take the first item
    prefix = switch.split('-')[0]
    
    # Split on '-' and take the second item
    suffix = switch.split('-')[1]
    
    # dc_code is first three characters of the prefix
    dc_code = prefix[0:3]
    
    # switch_function is first character of the suffix
    switch_function = suffix[0]
    
    # switch_number is last two characters of the suffix
    switch_number = suffix[-2:]
    
    print('{0}: DC:{1} FUNC:{2} NUMBER:{3}'.format(switch, dc_code, switch_function, switch_number))

print(len(switches), 'in switch list.')
