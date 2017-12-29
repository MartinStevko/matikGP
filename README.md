# Matik GP
Django project for correspondence seminars. Grand Prix of winter Matik 2018.

## Installation

### Windows
```cmd
pip install Django==2.0
```
```cmd
pip install virtualenvwrapper-win
```
### Linux
```cmd
sudo apt install pip
```
```cmd
pip install Django==2.0
```
```cmd
pip install virtualenvwrapper-win
```

## Work on project
For a first time
```cmd
mkvirtualenv matikgp
```
```cmd
manage.py makemigrations pokemoni
```
```cmd
manage.py migrate
```
and every time
```cmd
workon matikgp
```
or run a .bat file "run.bat" in "work_on_project" directory

## Changed across multiple reboots status

### Instalation
```terminal
sudo apt-get install git
git init
git config --global user.name "..."
git config --global user.email ...@gmail.com
sudo apt install pip
pip install --upgrade pip
sudo apt install virtualenv
virtualenv matik
source virtualenv/bin/activate
pip install django==1.8
git clone git://github.com/MartinStevko/matikgp.git
cd matikgp
```
