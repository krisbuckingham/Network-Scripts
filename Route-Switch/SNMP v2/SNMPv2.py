#This program opens a file with IP addresses. It SSH connects
#to each IP address in the first file and runs the commands. All output
#from each session is put into a text file with the IP address in the name

import getpass
from netmiko import ConnectHandler

#Collect Username, Password, and Enable from Prompt
user = input('Enter the Username:')
print('Enter Password')
password = getpass.getpass()
print('Enter enable password')
enable = getpass.getpass()
num_lines = sum(1 for line in open('switchlist.txt'))
#Open a list of IP addresses
a = open('switchlist.txt')
#For each IP address in the list, login to the device
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
    #Connect to the device	
    net_connect = ConnectHandler(**cisco_switch)
    #Run Commands
    cfg_commands = ['snmp-server community convergeoneSNMP','do wr',' do show run | sec SNMP']
    # send_config_set() will automatically enter/exit config mode
    output = net_connect.send_config_set(cfg_commands)
    print(output)
    net_connect.disconnect()
    num_lines -= 1
a.close()

