import subprocess
import sys
import os

try:
    os.system("net session > nul 2>&1")
except subprocess.CalledProcessError:
    print("Precisa de privilégios de administrador.")
    exit(0)

script_path = os.getcwd()
print(f"O script está sendo executado em {script_path}.")

for arquivo in os.listdir(script_path):
    if arquivo.startswith('veyon-') and arquivo.endswith('.exe'):
        veyon_setup_file = os.path.join(script_path, arquivo)
        break
print('Instalando Veyon...')

os.system(f'{veyon_setup_file} /S /NoMaster /NoStartMenuFolder')

veyon_cli_path = '"C:\\Program Files\\Veyon\\veyon-cli.exe"'
print(f'Veyon CLI path: {veyon_cli_path}')
print('Configurando Veyon...')
os.system(f'{veyon_cli_path} config import {os.path.join(script_path, "confs.json")}')

if sys.version_info:
    print("Python está instalado.")
    print("Versão do Python:", sys.version)
    python_path = sys.executable
    print('Instalando bibliotecas necessárias...')
    os.system(f'"python_path" -m pip install getmac')
    input('Pressione Enter para sair.')
    exit(0)
else:
    print('Python não está instalado. Instale o Python e instale o getmac com o comando "pip install getmac".')
    input('Pressione Enter para sair.')
    exit(0)