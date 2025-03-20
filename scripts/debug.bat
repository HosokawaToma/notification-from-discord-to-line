@echo off
setlocal

call scripts\base\export-requirements.bat

call scripts\base\delete.bat

call scripts\base\build.bat

call scripts\base\up.bat

call scripts\base\logs.bat < nul

call scripts\base\down.bat

echo [1;95mDebugging environment has been cleaned up.[0m
endlocal
