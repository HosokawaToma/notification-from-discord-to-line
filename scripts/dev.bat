@echo off
setlocal

call scripts\base\export-requirements.bat

call scripts\base\build.bat

call scripts\base\up.bat

call scripts\base\logs.bat < nul

call scripts\base\down.bat

echo [1;95mDevelopment environment is still running.[0m
endlocal
