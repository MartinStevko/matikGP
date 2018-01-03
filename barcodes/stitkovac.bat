@echo off
cd %~dp0

barcodes.py
pokeresolver.py
REM rename pokestitky.txt pokestitky.tex
REM latex pokekarty.tex -enable-pipes -interaction=nonstopmode -job-name=karticky.pdf -output-directory=. -src-specials

cd ..
