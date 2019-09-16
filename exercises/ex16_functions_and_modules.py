# Ex. 16

# Using functions in procedural code


def switch(name, hw_type, sw_version):
    s = {'name': name, 'hw_type': hw_type, 'sw_version': sw_version}
    return s


def print_switch(switch):
    print('Name:', switch['name'])
    print('Type:', switch['hw_type'])
    print('Version:', switch['sw_version'])
    print('+------------------------------------------------------------+')
    return
# When run as python script __name__ == '__main__'
# When run as import, __name__ == <import script name>
#
# cp ex16_functions_and_modules.py infra.py
# ipython
# import infra
# s1 = infra.switch('fra2-a10', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
#
#if __name__ == '__main__':
# Test code here
s1 = switch('fra2-a10', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
s2 = switch('chc1-a01', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
s3 = switch('chc1-a02', 'N9K-C93128TX', 'n9000-12.0(1q)' )

print_switch(s1)
print_switch(s2)
print_switch(s3)
