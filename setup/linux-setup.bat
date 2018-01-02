SET /P _inputname= Name of virtual enviroment: 
virtualenv %_inputname%
iptables -I INPUT -p tcp -m tcp --dport PORT_NUMBER -j ACCEPT
