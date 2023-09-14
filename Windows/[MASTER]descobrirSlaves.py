# Python 3 for Windows 11

from socket import *
import subprocess
import os

try:
    os.system("net session > nul 2>&1")
except subprocess.CalledProcessError:
    print("Precisa de privilégios de administrador.")
    exit(0)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

try:
    lab = gethostname().split('LAB')[1]
    print(f'Laboratório: LAB{lab}')
    print('A descoberta de novas máquinas está ativa! Aguardando envio das credenciais pelo slave...')
    
    while 1:
        connectionSocket, addr = serverSocket.accept()
        sentence = connectionSocket.recv(1024)
        newMachine = sentence.decode('ascii').split(',')
        print(f' {newMachine} ADICIONADO!')
        comando = f'"C:\\Program Files\\Veyon\\veyon-cli.exe" networkobjects add computer "{newMachine[0]}" "{newMachine[1]}" "{newMachine[2]}" "LAB{lab}"'
        subprocess.call(comando, shell=True)
        connectionSocket.send('Conexao bem sucedida!'.encode('ascii'))
        connectionSocket.close()
        
except IndexError:
    print('Não foi possível identificar o laboratório. Certifique-se de que o nome do computador está no formato PCPROFLAB...')