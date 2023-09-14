# Python 3 for Windows 11

import socket
from getmac import get_mac_address as gma
import subprocess
import os

try:
    os.system("net session > nul 2>&1")
except subprocess.CalledProcessError:
    print("Precisa de privilégios de administrador.")
    exit(0)

script_path = os.getcwd()
print(f"O script está sendo executado em {script_path}.")

lab = input("Informe o número do laboratório: ")

try:
    serverIP = socket.gethostbyname(f'PCPROFLAB{lab}')
    print(f"O IP do servidor é {serverIP}.")
except socket.gaierror:
    print("Não foi possível encontrar o servidor.")
    
confirmacao = input(f'Deseja se conectar ao servidor PCPROFLAB{lab}({serverIP})?')
if confirmacao.upper() != 'S':
    exit(0)
else:
    print('Conectando ao servidor...')
    veyon_cli_path = '"C:\\Program Files\\Veyon\\veyon-cli.exe"'
    print(f'Veyon CLI path: {veyon_cli_path}')
    print('Configurando Veyon...')
    os.system(f'{veyon_cli_path} authkeys import LAB{lab}/public {os.path.join(script_path, f"LAB{lab}.pem")}')

    # Enviar credenciais para o servidor
    serverPort = 12000
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIP, serverPort))

    hostName = socket.gethostname()
    hostIP = socket.gethostbyname(hostName)
    macAddr = gma()
    clientSocket.send((hostName+","+hostIP+","+macAddr).encode('ascii'))
    res = clientSocket.recv(1024)
    print(res.decode('ascii'))
    clientSocket.close()

    print('Credenciais enviadas.')
    input('Pressione Enter para sair.')