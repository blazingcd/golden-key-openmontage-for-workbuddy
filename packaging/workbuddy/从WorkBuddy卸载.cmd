@echo off
title Uninstall Golden Key OpenMontage for WorkBuddy
set "PS_EXE=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
if not exist "%PS_EXE%" set "PS_EXE=powershell.exe"
set "UNINSTALL_SCRIPT=%~dp0uninstall-workbuddy.ps1"
if exist "%TEMP%" cd /d "%TEMP%"
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -File "%UNINSTALL_SCRIPT%" %*
set "UNINSTALL_RESULT=%ERRORLEVEL%"
if not defined OPENMONTAGE_WORKBUDDY_NO_PAUSE pause >nul
exit /b %UNINSTALL_RESULT%
