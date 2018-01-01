cd %~dp0
cd ..
pause
manage.py makemigrations pokemoni
manage.py migrate
pause
manage.py createsuperuser
pause
create_database.py
pause

REM !!! tu este treba daco dat !!!

del init_database.txt
echo
echo Successful!
pause
