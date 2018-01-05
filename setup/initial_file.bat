@echo off
title Matik GP

cd %~dp0
cd ..
pause

manage.py makemigrations pokemoni
manage.py migrate
echo Migrations successfully created!
pause

manage.py createsuperuser
pause

%~dp0\create_database.py
manage.py shell < .\init_database.txt
del .\barcodes\init_database.txt
copy .\init_database.txt .\barcodes\init_database.txt
del .\init_database.txt
echo Database successfully created!
pause

break>"%~dp0\zaciatok.txt"
break>"%~dp0\koniec.txt"
echo Required files successfully created!
pause

manage.py runserver 0.0.0.0:80
