[CmdletBinding()]
param(
    [string]$InstallRoot,
    [string]$DataRoot,
    [string]$WorkBuddySkillsRoot
)

$ErrorActionPreference = 'Stop'

function Get-NormalizedPath {
    param([Parameter(Mandatory = $true)][string]$Path)

    return [IO.Path]::GetFullPath($Path).TrimEnd(
        [IO.Path]::DirectorySeparatorChar,
        [IO.Path]::AltDirectorySeparatorChar
    )
}

$sourceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
if ([string]::IsNullOrWhiteSpace($InstallRoot)) {
    $manifestPath = Join-Path $sourceRoot 'BUNDLE-MANIFEST.json'
    if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        throw 'InstallRoot is required when BUNDLE-MANIFEST.json is unavailable.'
    }
    $manifest = Get-Content -Raw -LiteralPath $manifestPath -Encoding UTF8 | ConvertFrom-Json
    $packageVersion = [string]$manifest.distribution.package_version
    $InstallRoot = Join-Path $env:LOCALAPPDATA "GoldenKeyOpenMontageForWorkBuddy\App\$packageVersion"
}

$InstallRoot = Get-NormalizedPath -Path $InstallRoot
if (-not (Test-Path -LiteralPath $InstallRoot -PathType Container)) {
    throw "Owned installation was not found and nothing was removed: $InstallRoot"
}
$volumeRoot = [IO.Path]::GetPathRoot($InstallRoot).TrimEnd('\', '/')
if ($InstallRoot.TrimEnd('\', '/') -eq $volumeRoot) {
    throw "Refusing to uninstall a volume root: $InstallRoot"
}
$recordPath = Join-Path $InstallRoot 'WORKBUDDY-INSTALL.json'
if (-not (Test-Path -LiteralPath $recordPath -PathType Leaf)) {
    throw "InstallRoot is not owned by Golden Key WorkBuddy and was preserved: $InstallRoot"
}
try {
    $record = Get-Content -Raw -LiteralPath $recordPath -Encoding UTF8 | ConvertFrom-Json
} catch {
    throw "InstallRoot ownership record is invalid and was preserved: $InstallRoot"
}
if ($record.schema_version -ne 'golden-key-workbuddy-install-v1') {
    throw "InstallRoot ownership record is not recognized and was preserved: $InstallRoot"
}
if ((Get-NormalizedPath -Path ([string]$record.install_root)) -ne $InstallRoot) {
    throw "InstallRoot ownership record points elsewhere and was preserved: $InstallRoot"
}

if ([string]::IsNullOrWhiteSpace($DataRoot)) {
    $DataRoot = [string]$record.data_root
}
if ([string]::IsNullOrWhiteSpace($WorkBuddySkillsRoot)) {
    $WorkBuddySkillsRoot = [string]$record.workbuddy_skills_root
}
$DataRoot = Get-NormalizedPath -Path $DataRoot
$WorkBuddySkillsRoot = Get-NormalizedPath -Path $WorkBuddySkillsRoot
$selfUninstall = (Get-NormalizedPath -Path $sourceRoot) -eq $InstallRoot
$deferredSelfCleanup = $selfUninstall -and $env:OS -eq 'Windows_NT'
if ((Get-NormalizedPath -Path ([string]$record.data_root)) -ne $DataRoot) {
    throw 'DataRoot does not match the owned installation record; nothing was removed.'
}
if ((Get-NormalizedPath -Path ([string]$record.workbuddy_skills_root)) -ne $WorkBuddySkillsRoot) {
    throw 'WorkBuddySkillsRoot does not match the owned installation record; nothing was removed.'
}
if ($InstallRoot -eq $DataRoot -or $InstallRoot -eq $WorkBuddySkillsRoot) {
    throw 'InstallRoot overlaps a preserved root; nothing was removed.'
}

$skillNames = @('golden-key-openmontage', 'golden-key-openmontage-onboarding')
$ownedSkills = @{}
$protectedSkills = @()
foreach ($skillName in $skillNames) {
    $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
    if (-not (Test-Path -LiteralPath $targetSkill)) {
        continue
    }
    $runtimePath = Join-Path $targetSkill 'WORKBUDDY-RUNTIME.json'
    if (-not (Test-Path -LiteralPath $runtimePath -PathType Leaf)) {
        $protectedSkills += $skillName
        continue
    }
    try {
        $runtime = Get-Content -Raw -LiteralPath $runtimePath -Encoding UTF8 | ConvertFrom-Json
        $owned = $runtime.schema_version -eq 'golden-key-workbuddy-runtime-location-v1' -and
            [string]$runtime.package_version -eq [string]$record.package_version -and
            (Get-NormalizedPath -Path ([string]$runtime.install_root)) -eq $InstallRoot
    } catch {
        $owned = $false
    }
    if ($owned) {
        $ownedSkills[$skillName] = $targetSkill
    } else {
        $protectedSkills += $skillName
    }
}

$skillBackups = @{}
$installParent = Split-Path -Parent $InstallRoot
$appBackup = Join-Path $installParent ('.uninstall-' + [Guid]::NewGuid().ToString('N'))
try {
    foreach ($skillName in $ownedSkills.Keys) {
        $backup = Join-Path $WorkBuddySkillsRoot ('.uninstall-' + $skillName + '-' + [Guid]::NewGuid().ToString('N'))
        Move-Item -LiteralPath $ownedSkills[$skillName] -Destination $backup
        $skillBackups[$skillName] = $backup
    }
    if ($deferredSelfCleanup) {
        $appBackup = $InstallRoot
    } else {
        Move-Item -LiteralPath $InstallRoot -Destination $appBackup
    }
} catch {
    foreach ($skillName in $skillBackups.Keys) {
        $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
        if (-not (Test-Path -LiteralPath $targetSkill) -and (Test-Path -LiteralPath $skillBackups[$skillName])) {
            Move-Item -LiteralPath $skillBackups[$skillName] -Destination $targetSkill
        }
    }
    throw
}

$cleanupWarnings = @()
$cleanupScheduled = $false
if ($deferredSelfCleanup) {
    $cleanupScriptRoot = Join-Path $DataRoot 'Temp'
    New-Item -ItemType Directory -Path $cleanupScriptRoot -Force | Out-Null
    $cleanupScript = Join-Path $cleanupScriptRoot ('finish-uninstall-' + [Guid]::NewGuid().ToString('N') + '.ps1')
    $escapedBackup = $appBackup.Replace("'", "''")
    $cleanupSource = @"
`$removed = `$false
for (`$attempt = 0; `$attempt -lt 60; `$attempt++) {
    try {
        if (Test-Path -LiteralPath '$escapedBackup') {
            Remove-Item -LiteralPath '$escapedBackup' -Recurse -Force -ErrorAction Stop
        }
        `$removed = -not (Test-Path -LiteralPath '$escapedBackup')
        if (`$removed) {
            break
        }
    } catch {
        # The launcher CMD or antivirus may briefly hold the install directory.
    }
    Start-Sleep -Milliseconds 500
}
Remove-Item -LiteralPath `$MyInvocation.MyCommand.Path -Force
"@
    Set-Content -LiteralPath $cleanupScript -Value $cleanupSource -Encoding UTF8
    $windowsPowerShell = Join-Path $env:SystemRoot 'System32\WindowsPowerShell\v1.0\powershell.exe'
    if (-not (Test-Path -LiteralPath $windowsPowerShell -PathType Leaf)) {
        $windowsPowerShell = 'powershell.exe'
    }
    Start-Process -FilePath $windowsPowerShell `
        -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$cleanupScript`"" `
        -WindowStyle Hidden | Out-Null
    $cleanupScheduled = $true
} else {
    try {
        Remove-Item -LiteralPath $appBackup -Recurse -Force
    } catch {
        $cleanupWarnings += "Program cleanup remains at: $appBackup"
    }
}
foreach ($skillName in $skillBackups.Keys) {
    try {
        Remove-Item -LiteralPath $skillBackups[$skillName] -Recurse -Force
    } catch {
        $cleanupWarnings += "Skill cleanup remains at: $($skillBackups[$skillName])"
    }
}

$report = [ordered]@{
    schema_version = 'golden-key-workbuddy-uninstall-v1'
    status = 'uninstalled'
    package_version = [string]$record.package_version
    install_root = $InstallRoot
    data_root = $DataRoot
    user_data_preserved = $true
    removed_skills = @($ownedSkills.Keys | Sort-Object)
    protected_skills = @($protectedSkills | Sort-Object)
    cleanup_warnings = $cleanupWarnings
    cleanup_scheduled = $cleanupScheduled
}
$logRoot = Join-Path $DataRoot 'Logs'
New-Item -ItemType Directory -Path $logRoot -Force | Out-Null
$reportPath = Join-Path $logRoot 'WORKBUDDY-LAST-UNINSTALL.json'
$report['report_path'] = $reportPath
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportPath -Encoding UTF8
$report | ConvertTo-Json -Depth 8
