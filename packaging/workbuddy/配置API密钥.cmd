@echo off
chcp 65001 >nul
title Configure Golden Key OpenMontage API Keys
set "PS_EXE=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
if not exist "%PS_EXE%" set "PS_EXE=powershell.exe"
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -File "%~dp0configure-provider-keys.ps1"
set "CONFIG_RESULT=%ERRORLEVEL%"
pause
exit /b %CONFIG_RESULT%
