# Python 3 for Windows 11

from socket import *
import subprocess, ctypes

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print('Need admin.')
    exit(1)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

lab = gethostname().split('LAB')[1]
print('Lab: ' + lab)

print('A descoberta de novas máquinas está ativa!')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    newMachine = sentence.decode('ascii').split(',')
    print(newMachine)
    commando = f'"C:/Program Files/Veyon/veyon-cli.exe" networkobjects add computer "{newMachine[0]}" "{newMachine[1]}" "{newMachine[2]}" "{lab}"'
    subprocess.call(commando, shell=True)
    connectionSocket.send("Ok!".encode('ascii'))
    connectionSocket.close()
