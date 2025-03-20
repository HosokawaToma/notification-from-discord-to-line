@echo off
setlocal

echo [1;95mExporting installed packages to requirements.txt...[0m
call venv\Scripts\activate
pip freeze > requirements.txt
deactivate

echo [1;95mrequirements.txt has been updated.[0m
endlocal
