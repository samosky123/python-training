from netmiko.arista import AristaSSH
import getpass
import sys


def main():
    device = raw_input('Device hostname or IP address: ')
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')

    if device and username and password:
        device_shell = AristaSSH(device, username=username, password=password)
        prompt = device_shell.find_prompt()
        device_shell.disable_paging()

        output = device_shell.send_command_expect('show ver', expect_string=prompt)

        device_shell.disconnect()

        output_line_list = output.split('\n')

        print output_line_list

        for line in output_line_list:

            if 'Software image' in line:
                eos = line.split(':')[1].strip()
                print 'Software version:', eos

    else:
        print 'No device, username or password provided'
        sys.exit(1)

if __name__ == '__main__':
    main()

# Exercise:
# - run interface status command or any other and print information based on a certain condition
# - can output command in json or xml depending on the supported option on a target device
