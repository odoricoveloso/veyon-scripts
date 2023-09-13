REM Veyon Master

net session 1>NUL 2>NUL || (echo Need Admin. & Exit /b 1)

set /p lab="Informe o numero do laboratorio: "

choice /c sn /n /m "Voce deseja renomear o host de %computername% para PCPROFLAB%lab%? Isso facilitara as instalacoes dos slaves. [SN]"
if %errorlevel% equ 1 goto renamePC
if %errorlevel% equ 2 goto finish

:renamePC
wmic computersystem where name="%computername%" call rename name="PCPROFLAB%lab%"

%~dp0veyon-4.8.2.0-win64-setup.exe /S

set veyon-cli="C:\Program Files\Veyon\veyon-cli.exe"
%veyon-cli% config import %~dp0confs.json
%veyon-cli% authkeys create "LAB%lab%"
%veyon-cli% authkeys export "LAB%lab%/public" "%~dp0LAB%lab%.pem"
%veyon-cli% networkobjects add location "LAB%lab%"

:finish
echo Você deve reiniciar o computador para que as configurações sejam aplicadas.
pause