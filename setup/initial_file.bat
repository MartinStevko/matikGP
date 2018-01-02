@echo off
title Matik GP

cd %~dp0
cd ..
pause

manage.py makemigrations pokemoni
manage.py migrate
pause

manage.py createsuperuser
pause

create_database.py
manage.py shell < init_database.txt
del init_database.txt
echo Successfully created!
pause

manage.py runserver 0.0.0.0:80
