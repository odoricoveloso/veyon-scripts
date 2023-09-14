#!/usr/bin/python3

from socket import *
import os

if(os.geteuid() != 0):
    print("You must be root!")
    exit(1)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

lab = gethostname().split('LAB')[1]
print('Lab: ' + lab)

print('Discovery of new slaves ready!')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    newMachine = sentence.decode('ascii').split(',')
    print(newMachine)
    os.system(f'veyon-cli networkobjects add computer "{newMachine[0]}" "{newMachine[1]}" "{newMachine[2]}" "LAB{lab}" 2>/dev/null')
    connectionSocket.send("Conexao bem sucedida!".encode('ascii'))
    connectionSocket.close()
