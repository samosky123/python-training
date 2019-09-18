import netmiko
import sys
import argparse
import datetime
import logging

def main():
    logfile = 'ex22b.log'
    logging.basicConfig(filename=logfile,
                        level=logging.DEBUG,
                        format="%(asctime)s %(levelname)s - %(message)s")
    parser = argparse.ArgumentParser(description="Network configuration script.")
    parser.add_argument("-device", help="Hostname or IP address of the target device.")
    parser.add_argument("-config_file", help="Configuration file.")
    parser.add_argument("-output_log", help="Output log, by default stored in output.log", default='output_log')

    args = parser.parse_args()
    print('Args:\n', args)

    if not args.device and not args.config_file:
        sys.exit('ERROR: Script expects device and configuration file.')

    try:
        config = []
        with open(args.config_file, 'r') as config_file:
            config = config_file.readlines()

        print(datetime.datetime.now(), 'Connecting to device')
        ssh = netmiko.ConnectHandler(device_type='cisco_nxos', ip=args.device, username='admin', 
                                     global_delay_factor=0.1, password='admin', timeout=10)

        ssh.enable()

        ssh.config_mode()
        print(datetime.datetime.now(), 'Configuring device')
        output = ''
        for cmd in config:
            if cmd and not cmd.startswith('!'):
                output += ssh.send_command(cmd, expect_string='#', auto_find_prompt=False,
                                           delay_factor = 0.1, strip_command=False, strip_prompt=False)
        #output = ssh.send_config_from_file(args.config_file, delay_factor=0)

        print(datetime.datetime.now(), 'Configured device')
       
         
        with open(args.output_log, 'w') as outfile:
            outfile.write(output)

        ssh.disconnect()

    except Exception as error:
        sys.exit('ERROR:' + str(error))

if __name__ == '__main__':
    main()
