REM Veyon

net session 1>NUL 2>NUL || (echo Need Admin. & Exit /b 1)

%~dp0veyon-4.8.2.0-win64-setup.exe /S /NoMaster /NoStartMenuFolder

set veyon-cli="C:\Program Files\Veyon\veyon-cli.exe"
%veyon-cli% config import %~dp0confs.json

"C:\Program Files\Python311\python.exe" -m pip install getmac

echo "Finished!"
