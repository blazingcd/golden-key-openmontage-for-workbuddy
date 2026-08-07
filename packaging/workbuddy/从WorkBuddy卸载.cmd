@echo off
title Uninstall Golden Key OpenMontage for WorkBuddy
set "PS_EXE=%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe"
if not exist "%PS_EXE%" set "PS_EXE=powershell.exe"
"%PS_EXE%" -NoProfile -ExecutionPolicy Bypass -File "%~dp0uninstall-workbuddy.ps1" %*
set "UNINSTALL_RESULT=%ERRORLEVEL%"
if not defined OPENMONTAGE_WORKBUDDY_NO_PAUSE pause >nul
exit /b %UNINSTALL_RESULT%
