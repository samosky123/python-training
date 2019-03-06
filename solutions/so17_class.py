#!/usr/bin/env python
# So. 17

# Using object-orientated code


class Switch():

    DC = {'fra2': {'desc': 'Equinix, Frankfurt'},
          'chc1': {'desc': 'Telx, Cermak, Chicago'}}

    def __init__(self, name, hw_type, sw_version):
        self.name = name
        self.hw_type = hw_type
        self.sw_version = sw_version

    def print_switch(self):
        sw_out = 'Name: ' + self.name + '\n'
        sw_out += 'Type:' + self.hw_type + '\n'
        sw_out += 'Version:' + self.sw_version + '\n'
        sw_out += '+------------------------------------------------------------+\n'
        return sw_out

    def dc(self):
        try:
            # Split on '-' and take the first item
            prefix = self.name.split('-')[0]
            # dc_code is first four characters of the prefix
            dc_code = prefix[0:4]
            dc_desc = self.DC[dc_code]['desc']
            return dc_desc
        except:
            return "unknown"


if __name__ == '__main__':
    # Test code here
    s1 = Switch('fra2-a10', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
    s2 = Switch('chc1-a01', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
    s3 = Switch('chc2-a02', 'N9K-C93128TX', 'n9000-12.0(1q)' )

    print s1.name, 'is in', s1.dc()
    print s2.name, 'is in', s2.dc()
    print s3.name, 'is in', s3.dc()
