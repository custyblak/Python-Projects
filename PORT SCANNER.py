#!usr/bin/python

# Port Scanner Script
import socket

host_name = input("Enter the target host domain name: ")
target_IP = socket.gethostbyname(host_name)

print(target_IP)

while True:
    target_port = int(input("Enter target port: "))
    try:
        soc = socket.socket()
        res = soc.connect((target_IP, target_port))
        print(f'Port {target_port} : Open')
        soc.close()

    except:
        print(f'Port {target_port} : Closed')
    break

print('Port scan completed')

