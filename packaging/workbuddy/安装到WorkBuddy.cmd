@echo off
call "%~dp0bootstrap\install-to-workbuddy.cmd" %*
exit /b %ERRORLEVEL%
