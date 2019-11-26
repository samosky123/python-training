import argparse
import sys

def main():

    parser = argparse.ArgumentParser(description="Network info script.")
    parser.add_argument("-device", help="Hostname or IP address of the target device.")
    parser.add_argument("-op", help="Operation to perform.", choices=['precheck', 'postcheck'])
    parser.add_argument("-v", "-verbose", help="increase output verbosity.", action="store_true")

    args = parser.parse_args()
    
    if not args.device or not args.op:
        print('ERROR: Device and Operation must be provided')
        sys.exit(1)

    if args.v:
        print('Device:', args.device)
        print('Operation:', args.op)
        print('Verbose:', args.v)
        print('\n')

    print('Processing Device: {0}, Operation: {1}'.format(str(args.device), args.op))

if __name__ == '__main__':
    main()

# Exercise:
# - add option of list of devices (file name)
# - validate that only device or list are entered, but not both
# - test that file with list of devices exists and print devices
