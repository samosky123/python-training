# Ex. 17

# Using object-orientated code


class Switch():
    def __init__(self, name, hw_type, sw_version):
        self.name = name
        self.hw_type = hw_type
        self.sw_version = sw_version

    def print_switch(self):
        print('Name:', self.name)
        print('Type:', self.hw_type)
        print('Version:', self.sw_version)
        print('+------------------------------------------------------------+')
        return

if __name__ == '__main__':
    # Test code here
    s1 = Switch('fra2-a10', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
    s2 = Switch('chc1-a01', 'N9K-C9372PX-E', 'n9000-12.0(1q)')
    s3 = Switch('chc1-a02', 'N9K-C93128TX', 'n9000-12.0(1q)' )

    s1.print_switch()
    s2.print_switch()
    s3.print_switch()

# Exercise. Add method to print DC information
#
# Clue. Add method
#
#    def dc(self):
        # Extract dc_code from self.name
        # Return the code or a description...
        #   ie Chicago for chc1, Frankfurt for fra2 etc
        # Take care or errors (try except)

