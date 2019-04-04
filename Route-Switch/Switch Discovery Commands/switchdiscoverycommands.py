import getpass
from netmiko import ConnectHandler

user = input('Enter the Username:')
print('Enter Password')
password = getpass.getpass()
print('Enter enable password')
enable = getpass.getpass()
a = open('switchlist.txt')
for IP in a:
    IP = IP.strip()
    print ('Reading Switch ' + IP)
    cisco_switch = {
    'device_type': 'cisco_ios',
    'ip':   IP,
    'username': user,
    'password': password,
	'secret': enable
	}	
    net_connect = ConnectHandler(**cisco_switch)
    b = open('commandlist.txt')
    for CMD in b:
        output = net_connect.send_command(CMD)
        print(output)
        f = open('Switch-Config ' + IP + '.txt', 'a')
        f.write(output)
        f.close()
    b.close()
a.close()

