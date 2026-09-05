@echo off
setlocal EnableExtensions DisableDelayedExpansion
chcp 65001 >nul

set "GK_PACKAGE=%~dp0GoldenKeyOpenMontageForWorkBuddy"
set "GK_PYTHON=%GK_PACKAGE%\bootstrap\python\python.exe"
set "GK_ADAPTER=%GK_PACKAGE%\shell-adapter"
if not exist "%GK_PYTHON%" goto invalid
if not exist "%GK_ADAPTER%\golden_key_openmontage_workbuddy\installer.py" goto invalid

"%GK_PYTHON%" -I -c "import sys;sys.path.insert(0,sys.argv.pop(1));from golden_key_openmontage_workbuddy.installer import _main;raise SystemExit(_main())" "%GK_ADAPTER%" ui-install --package-root "%GK_PACKAGE%"
exit /b %errorlevel%

:invalid
echo 安装包不完整。请重新解压整个 ZIP 后再运行此文件。
exit /b 1
