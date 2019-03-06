#!/usr/bin/env python
import argparse
import sys


def args_parser():

    parser = argparse.ArgumentParser(description="Network info script.")
    parser.add_argument("-device", help="Hostname or IP address of the target device.")
    parser.add_argument("-list", help="List of Devices (Hostname or IP address)")
    parser.add_argument("-op", help="Operation to perform.", choices=['precheck', 'postcheck'])
    parser.add_argument("-cmds", help="File with list of commands")
    parser.add_argument("-outdir", help="Output directory", default='out')
    parser.add_argument("-v", "-verbose", help="increase output verbosity.", action="store_true")

    args = parser.parse_args()

    if args.device and args.list:
        print 'ERROR: Only Device or List are allowed option.'
        sys.exit(1)

    elif not args.device and not args.list:
        print 'ERROR: Device or List of devices must be provided.'
        sys.exit(1)

    if not args.op:
        print 'ERROR: Operation must be provided.'
        sys.exit(1)

    if not args.cmds:
        print 'ERROR: File with list of commands must be provided.'
        sys.exit(1)

    return args


def parse_file(filename):

    output_list = []

    try:
        file = open(filename, "r")
        output = file.readlines()
        file.close()

    except Exception as error:
        print 'ERROR: Failed to open and parse file', filename
        sys.exit(1)

    for line in output:
        if line:
            output_list.append(line.strip())

    return output_list


def main():

    args = args_parser()

    device_list = []

    if args.list:

        device_list = parse_file(args.list)

    elif args.device:
        device_list.append(args.device)

    if args.v:
        print 'Script Parameters (verbose output):'
        print '  List:' + str(args.list)
        print '  Device:' + str(args.device)
        print '  Operation:' + str(args.op)
        print '  Commands File: ' + str(args.cmds)
        print '  Output Dir:' + str(args.outdir)
        print '  Verbose:' + str(args.v)
        print '==============================='

    for device in device_list:
        print 'Processing Device: {0}'.format(device)

if __name__ == '__main__':
    main()
