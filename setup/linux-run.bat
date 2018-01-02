@echo off
cd %~dp0
cd -
SET /P _inputname= Name of virtual enviroment: 
source %_inputname%/bin/activate
SET /P _portnumber= Port number (80 - Hypertext Transfer Protocol (WWW)): 
python manage.py runserver 0.0.0.0:%portnumber%
