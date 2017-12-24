@echo off
start chrome.exe https://github.com/MartinStevko/matikgp
start chrome.exe https://docs.djangoproject.com/en/2.0/

start %~dp0

title Matik GP
cd %~dp0
workon matikgp

pause >nul
