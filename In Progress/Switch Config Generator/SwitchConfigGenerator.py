#This program opens two files, one with IP addresses and one with commands. It SSH connects
#to each IP address in the first file and runs the commands on the second file. All output
#from each session is put into a text file with the IP address in the name

import csv

#Open the CSV file
with open('District Inventory Worksheet.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    data = list(csvreader)

data.pop(0)
for row in data:

    if "n/a" in row:
        print("SFP - Skip")

    elif "Stack Standby" in row:
        print("Standby Switch Skip")

    else:
        # print('hello')
        # f = open('testfile.txt', 'a')
        # f.write('management ip ' + row[4])
        # f.close()
        # print(row[7])
        f = open(row[7] + 'config' + '.txt', 'a')
        f.write('interface vlan ' + row[3] + '\r')
        f.write('ip address ' + row[4] + ' ' + row[5])
        f.write('exit')
        f.close()



#Collect Username, Password, and Enable from Prompt
# user = input('Enter the Username:')
# print('Enter Password')
# password = getpass.getpass()
# print('Enter enable password')
# enable = getpass.getpass()
# num_lines = sum(1 for line in open('iplist.txt'))
# #Open a list of IP addresses
# a = open('iplist.txt')
# #For each IP address in the list, login to the device
# for IP in a:
#     IP = IP.strip()
#     print ('Assessing Device ' + IP + '. ' + str(num_lines) + ' devices remaining')
#     cisco_switch = {
#     'device_type': 'cisco_ios',
#     'ip':   IP,
#     'username': user,
#     'password': password,
# 	'secret': enable
# 	}	
#     #Connect to the device
#     net_connect = ConnectHandler(**cisco_switch)
#     #Open a list of commands
#     b = open('commandlist.txt')
#     for CMD in b:
#         #Run each command, write to a txt file the output
#         output = ('\n-------- ' + CMD.strip() + ' --------\n')
#         output += net_connect.send_command(CMD)
#         print(output)
#         f = open('Device-Config ' + IP + '.txt', 'a')
#         f.write(output)
#         f.close()
#     b.close()
#     num_lines -= 1
# a.close()