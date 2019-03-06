import paramiko
import getpass
import sys
from time import sleep


def main():
    device = raw_input('Device hostname or IP address: ')
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')

    if device and username and password:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(device, username=username, password=password, look_for_keys=False)
        device_shell = ssh.invoke_shell()

        # sleep 3 seconds to ensure we are in prompt
        sleep(3)

        if device_shell.recv_ready():
            device_shell.recv(9999)

        # disable pagination
        device_shell.send('term len 0\n')

        sleep(1)

        # Prompt discovery

        prompt = ''
        device_shell.send('\n')
        sleep(.5)

        while True:
            if device_shell.recv_ready():
                prompt = device_shell.recv(9999).split('\n')[-1]
                break

        device_shell.send('show ver\n')
        output = ''
        while True:
            if device_shell.recv_ready():

                output += device_shell.recv(9999)

                if output.endswith(prompt):
                    break

        ssh.close()

        output_line_list = output.split('\n')

        for line in output_line_list:
            # print line
            if 'Software image' in line:
                eos = line.split(':')[1].strip()
                print 'Software version:', eos

    else:
        print 'No device, username or password provided'
        sys.exit(1)

if __name__ == '__main__':
    main()

# Exercise:
# - run interface status command, print interfaces in Up status
