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

zenity --question --width=320 --title "Renomear Computador" \
--text="Você deseja renomear o host para PCPROFLAB$lab? Isso facilitará as instalações dos slaves."
if [ "$?" == "0" ]; then
    pcName="PCPROFLAB$lab"
    echo "$pcName" > /etc/hostname
    sed -i "/127.0.1.1/c\127.0.1.1\t$pcName" /etc/hosts
fi

echo "Caso demorar aqui, pressione ENTER!"

add-apt-repository ppa:veyon/stable -y
apt install veyon -y

sed -i '/Exec=/c\Exec=sudo /usr/bin/veyon-master' /usr/share/applications/veyon-master.desktop
sed -i '/Terminal=false/c\Terminal=true' /usr/share/applications/veyon-master.desktop

veyon-cli config import scriptPath/confs.json
veyon-cli authkeys create LAB$lab
veyon-cli authkeys export LAB$lab/public scriptPath/LAB$lab.pem

veyon-cli networkobjects add location "LAB$lab"

echo Você deve reiniciar o computador para que as configurações sejam aplicadas.
echo "Pressione Enter para sair..."
read