#!/usr/bin/python3
from socket import *
import psutil
import sys

serverName = sys.argv[1]
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( (serverName, serverPort) )

hostName = gethostname()
for interface, addrs in psutil.net_if_addrs().items():
    if interface != 'lo':
        hostIP = addrs[0].address
        macAddr = addrs[1].address
        break
else:
    print("Nenhuma interface de rede encontrada (exceto loopback).")
    sys.exit(1)

clientSocket.send((hostName+","+hostIP+","+macAddr).encode('ascii'))
res = clientSocket.recv(1024)
print(res.decode('ascii'))
clientSocket.close()