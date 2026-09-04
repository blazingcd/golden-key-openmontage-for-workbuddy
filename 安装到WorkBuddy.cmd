@echo off
setlocal EnableExtensions DisableDelayedExpansion
chcp 65001 >nul

rem The verified private Python is inside the release, so only inbox PowerShell is trusted before extraction.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "$admin=([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator); if($admin){exit 0}else{exit 1}"
if not errorlevel 1 goto elevated
set "GK_SELF=%~f0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "$p=Start-Process -FilePath $env:GK_SELF -ArgumentList '--elevated' -Verb RunAs -Wait -PassThru; exit $p.ExitCode"
exit /b %errorlevel%

:elevated

set "GK_RELEASE_ROOT=%~dp0"
for /f "usebackq delims=" %%I in (`powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "$root=[IO.Path]::GetFullPath($env:GK_RELEASE_ROOT); $sidecars=@(Get-ChildItem -LiteralPath $root -File -Filter '*.zip.sha256'); if($sidecars.Count -ne 1){throw 'release sidecar count'}; $sidecar=$sidecars[0]; $zip=$sidecar.FullName.Substring(0,$sidecar.FullName.Length-7); if(-not (Test-Path -LiteralPath $zip -PathType Leaf)){throw 'release missing'}; $line=(Get-Content -LiteralPath $sidecar.FullName -Raw).Trim(); if($line -notmatch '^([0-9a-fA-F]{64}) \*(.+\.zip)$'){throw 'sidecar format'}; $name=$matches[2]; if($name.IndexOfAny([IO.Path]::GetInvalidFileNameChars()) -ge 0 -or $name -cne [IO.Path]::GetFileName($zip)){throw 'sidecar name'}; if((Get-FileHash -LiteralPath $zip -Algorithm SHA256).Hash -ine $matches[1]){throw 'release hash'}; [Console]::Out.WriteLine($zip)"`) do set "GK_RELEASE=%%I"
if not defined GK_RELEASE (
  echo 安装包校验失败。现有程序和用户数据未改动。
  exit /b 1
)

for /f "usebackq delims=" %%I in (`powershell.exe -NoProfile -Command ^
  "[Console]::Out.WriteLine([IO.Path]::Combine([IO.Path]::GetTempPath(),'GoldenKeyOpenMontageForWorkBuddy-'+[guid]::NewGuid().ToString('N')))"`) do set "GK_BOOT=%%I"
if not defined GK_BOOT exit /b 1

powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "Expand-Archive -LiteralPath $env:GK_RELEASE -DestinationPath $env:GK_BOOT"
if errorlevel 1 goto cleanup

set "GK_PACKAGE=%GK_BOOT%\GoldenKeyOpenMontageForWorkBuddy"
set "GK_PYTHON=%GK_PACKAGE%\bootstrap\python\python.exe"
set "GK_ADAPTER=%GK_PACKAGE%\shell-adapter"
if not exist "%GK_PYTHON%" goto cleanup
if not exist "%GK_ADAPTER%\golden_key_openmontage_workbuddy\installer.py" goto cleanup

"%GK_PYTHON%" -I -c "import sys;sys.path.insert(0,sys.argv.pop(1));from golden_key_openmontage_workbuddy.installer import _main;raise SystemExit(_main())" "%GK_ADAPTER%" ui-install --release-archive "%GK_RELEASE%"
set "GK_EXIT=%errorlevel%"
goto cleanup_done

:cleanup
set "GK_EXIT=1"

:cleanup_done
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command ^
  "$target=[IO.Path]::GetFullPath($env:GK_BOOT); $base=[IO.Path]::GetFullPath([IO.Path]::GetTempPath()); if(-not $target.StartsWith($base,[StringComparison]::OrdinalIgnoreCase) -or [IO.Path]::GetFileName($target) -notlike 'GoldenKeyOpenMontageForWorkBuddy-*'){exit 1}; if(Test-Path -LiteralPath $target){Remove-Item -LiteralPath $target -Recurse -Force}"
exit /b %GK_EXIT%
