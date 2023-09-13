REM Join to Veyon Master

net session 1>NUL 2>NUL || (echo Need Admin. & Exit /b 1)

set /p lab="Informe o numero do laboratorio: "

python -c "import socket,sys;sys.stdout.write(socket.gethostbyname('PCPROFLAB%lab%'))" > %temp%\ipadr
set /p masterPC= < %temp%\ipadr

choice /c sn /n /m "Voce deseja se conectar ao servidor mestre padrao (%masterPC%)? [SN]"
if %errorlevel% equ 1 goto joinLocation
if %errorlevel% equ 2 goto finish

:joinLocation
set veyon-cli="C:\Program Files\Veyon\veyon-cli.exe"
%veyon-cli% authkeys import "LAB%lab%/public" "%~dp0LAB%lab%.pem"
python %~dp0[SLAVE]ingressarGrupo.py %masterPC%

:finish
pause