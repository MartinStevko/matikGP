# Server setup for local network (on linux machine)

## Prerequisites

1. Cloned matikgp project
2. Python virtual environment set up and django installed

## Procedure

1. Login as root user
2. Activate virtual environment
3. Allow remote acces for desired port:
```bash
iptables -I INPUT -p tcp -m tcp --dport PORT_NUMBER -j ACCEPT
```
4. Run server on your desired port:
```bash
python manage.py runserver 0.0.0.0:PORT_NUMBER
```
