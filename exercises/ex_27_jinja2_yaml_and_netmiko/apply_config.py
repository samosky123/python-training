import netmiko

with open("configs/arista-conf") as fconf:
    cli_config = fconf.readlines()

ssh = netmiko.ConnectHandler(device_type='cisco_ios', ip='10.9.100.201', username='admin', 
                             global_delay_factor=0.1, password='admin', timeout=10)

ssh.enable()
ssh.config_mode()

output = ''
for cmd in cli_config:
    if cmd and not cmd.startswith('!'):
        output += ssh.send_command(cmd, expect_string='#', auto_find_prompt=False,
                  delay_factor = 0.1, strip_command=False, strip_prompt=False)

ssh.disconnect()

print('OUTPUT:', output)
