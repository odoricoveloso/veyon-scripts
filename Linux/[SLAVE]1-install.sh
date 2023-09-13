#!/bin/bash

#
# https://docs.veyon.io/en/latest/admin/cli.html
#

scriptPath="$PWD"

if [ "$(id -u)" != "0" ]; then
    echo "You must be root!"
    exit 1
fi

echo "Informe o numero do laboratorio: "
read lab

masterPC="PCPROFLAB$lab"
zenity --question --width=300 --title="Alterar mestre" --text="Você deseja se conectar ao servidor mestre padrão ($masterPC)?"
if [ "$?" == "1" ]; then
    masterPC=$(zenity --entry --width=300 --title="hostname do master" --text="Digite o hostname do mestre")
    echo "Usando servidor $masterPC"
fi

add-apt-repository ppa:veyon/stable -y
apt install veyon -y

veyon-cli config import scriptPath/confs.json
veyon-cli authkeys import LAB$lab/public scriptPath/LAB$lab.pem

sleep 2
systemctl restart veyon.service

sleep 2
apt install python3 python3-pip -y
pip3 install psutil

python3 scriptPath/[SLAVE]2-ingressarGrupo.py $masterPC

rm /usr/share/applications/veyon-configurator.desktop
rm /usr/share/applications/veyon-master.desktop

echo "Pressione Enter para sair..."
read