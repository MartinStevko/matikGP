@echo off
SET /P _inputname= Name of virtual enviroment:
py -m venv %_inputname%
