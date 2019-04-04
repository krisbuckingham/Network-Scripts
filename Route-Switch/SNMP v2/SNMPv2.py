import getpass
from netmiko import ConnectHandler

user = input('Enter the Username:')
print('Enter Password')
password = getpass.getpass()
print('Enter enable password')
enable = getpass.getpass()
num_lines = sum(1 for line in open('switchlist.txt'))
a = open('switchlist.txt')
for IP in a:
    IP = IP.strip()
    print ('Configuring SNMP on ' + IP + '. ' + str(num_lines) + ' devices remaining')
    cisco_switch = {
    'device_type': 'cisco_ios',
    'ip':   IP,
    'username': user,
    'password': password,
	'secret': enable
	}	
    net_connect = ConnectHandler(**cisco_switch)
    cfg_commands = ['snmp-server community convergeoneSNMP','do wr',' do show run | sec SNMP']
    # send_config_set() will automatically enter/exit config mode
    output = net_connect.send_config_set(cfg_commands)
    print(output)
    net_connect.disconnect()
    num_lines -= 1
a.close()

