@echo off

net session 1>NUL 2>NUL || (echo Need Admin. & Exit /b 1)

cd %~dp0

python [MASTER]descobrirSlaves.py
