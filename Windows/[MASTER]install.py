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

rename_choice = input(f"Você deseja renomear o host de {os.environ['COMPUTERNAME']} para PCPROFLAB{lab}? Isso facilitará as instalações dos slaves. [S/N]: ").upper()
if rename_choice == 'S':
    print(f'Renomeando host para PCPROFLAB{lab}...')
    os.system(f'wmic computersystem where name="{os.environ["COMPUTERNAME"]}" call rename name="PCPROFLAB{lab}"')

    for arquivo in os.listdir(script_path):
        if arquivo.startswith('veyon-') and arquivo.endswith('.exe'):
            veyon_setup_file = os.path.join(script_path, arquivo)
            break
    print('Instalando Veyon...')
    os.system(f'{veyon_setup_file} /S')

    veyon_cli_path = '"C:\\Program Files\\Veyon\\veyon-cli.exe"'
    print(f'Veyon CLI path: {veyon_cli_path}')
    print('Configurando Veyon...')
    os.system(f'{veyon_cli_path} config import {os.path.join(script_path, "confs.json")}')
    os.system(f'{veyon_cli_path} authkeys create LAB{lab}')
    os.system(f'{veyon_cli_path} authkeys export LAB{lab}/public {os.path.join(script_path, f"LAB{lab}.pem")}')
    os.system(f'{veyon_cli_path} authkeys export LAB{lab}/private {os.path.join(script_path, f"LAB{lab}.key")}')
    os.system(f'{veyon_cli_path} networkobjects add location LAB{lab}')

    print('Você deve reiniciar o computador para que as configurações sejam aplicadas.')
    input('Pressione Enter para sair.')
    exit(0)
else:
    print(f'Configurações não aplicadas.')
    input('Pressione Enter para sair.')
    exit(0)
