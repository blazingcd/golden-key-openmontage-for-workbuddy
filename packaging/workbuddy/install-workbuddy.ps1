[CmdletBinding()]
param(
    [string]$InstallRoot = (Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\App\0.1.0-prealpha.1'),
    [string]$DataRoot = (Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\Data'),
    [string]$WorkBuddySkillsRoot = (Join-Path $env:USERPROFILE '.workbuddy\skills')
)

$ErrorActionPreference = 'Stop'

function Get-FileSha256 {
    param([Parameter(Mandatory = $true)][string]$Path)

    $stream = [IO.File]::Open(
        $Path,
        [IO.FileMode]::Open,
        [IO.FileAccess]::Read,
        [IO.FileShare]::Read
    )
    try {
        $hasher = [Security.Cryptography.SHA256]::Create()
        try {
            return ([BitConverter]::ToString($hasher.ComputeHash($stream))).Replace('-', '').ToLowerInvariant()
        } finally {
            $hasher.Dispose()
        }
    } finally {
        $stream.Dispose()
    }
}

$sourceRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$manifestPath = Join-Path $sourceRoot 'BUNDLE-MANIFEST.json'
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw 'BUNDLE-MANIFEST.json is missing. Extract the complete ZIP before registration.'
}

$manifest = Get-Content -Raw -LiteralPath $manifestPath -Encoding UTF8 | ConvertFrom-Json
if ($manifest.distribution.status -ne 'first_installer_build_validation_only') {
    throw 'This installer only accepts the declared first-build validation package.'
}

$sourceRootFull = [IO.Path]::GetFullPath($sourceRoot).TrimEnd([IO.Path]::DirectorySeparatorChar, [IO.Path]::AltDirectorySeparatorChar)
$declaredFiles = @{}
foreach ($entry in $manifest.files) {
    $declaredPath = ([string]$entry.path).Replace('\', '/')
    if ([string]::IsNullOrWhiteSpace($declaredPath) -or
        [IO.Path]::IsPathRooted($declaredPath) -or
        ($declaredPath.Split('/') -contains '..')) {
        throw "Unsafe package file path: $declaredPath"
    }
    $relative = $declaredPath.Replace('/', [IO.Path]::DirectorySeparatorChar)
    $candidate = [IO.Path]::GetFullPath((Join-Path $sourceRootFull $relative))
    if (-not $candidate.StartsWith($sourceRootFull + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Package file escapes the extracted directory: $declaredPath"
    }
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "Package file is missing: $declaredPath"
    }
    $actual = Get-FileSha256 -Path $candidate
    if ($actual -ne ([string]$entry.sha256).ToLowerInvariant()) {
        throw "Package file hash mismatch: $declaredPath"
    }
    $declaredFiles[$declaredPath] = $candidate
}

$extraFiles = @(
    Get-ChildItem -LiteralPath $sourceRootFull -File -Recurse -Force |
        ForEach-Object {
            $relative = $_.FullName.Substring($sourceRootFull.Length).TrimStart('\', '/').Replace('\', '/')
            if ($relative -ne 'BUNDLE-MANIFEST.json' -and -not $declaredFiles.ContainsKey($relative)) {
                $relative
            }
        } |
        Sort-Object
)

$skillNames = @('golden-key-openmontage', 'golden-key-openmontage-onboarding')
$operation = 'fresh_install'
$installRootExists = Test-Path -LiteralPath $InstallRoot
if ($installRootExists) {
    if (-not (Test-Path -LiteralPath $InstallRoot -PathType Container)) {
        throw "InstallRoot is not a directory and cannot be repaired: $InstallRoot"
    }
    $existingInstallRecordPath = Join-Path $InstallRoot 'WORKBUDDY-INSTALL.json'
    if (-not (Test-Path -LiteralPath $existingInstallRecordPath -PathType Leaf)) {
        throw "InstallRoot is not owned by Golden Key WorkBuddy and was preserved: $InstallRoot"
    }
    try {
        $existingInstallRecord = Get-Content -Raw -LiteralPath $existingInstallRecordPath -Encoding UTF8 | ConvertFrom-Json
    } catch {
        throw "InstallRoot ownership record is invalid and was preserved: $InstallRoot"
    }
    if ($existingInstallRecord.schema_version -ne 'golden-key-workbuddy-install-v1') {
        throw "InstallRoot ownership record is not recognized and was preserved: $InstallRoot"
    }
    $existingVersion = [string]$existingInstallRecord.package_version
    $incomingVersion = [string]$manifest.distribution.package_version
    if ([string]::IsNullOrWhiteSpace($existingVersion) -or $existingVersion -ne $incomingVersion) {
        throw "Cross-version replacement is not enabled; existing=$existingVersion incoming=$incomingVersion. Existing install was preserved."
    }
    $operation = 'repair'
}

$existingOwnedSkills = @{}
foreach ($skillName in $skillNames) {
    $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
    if (Test-Path -LiteralPath $targetSkill) {
        if (-not (Test-Path -LiteralPath $targetSkill -PathType Container)) {
            throw "WorkBuddy Skill path is not a directory and was preserved: $targetSkill"
        }
        $runtimeMarker = Join-Path $targetSkill 'WORKBUDDY-RUNTIME.json'
        if (-not (Test-Path -LiteralPath $runtimeMarker -PathType Leaf)) {
            throw "A foreign WorkBuddy Skill uses the Golden Key name and was preserved: $targetSkill"
        }
        try {
            $existingRuntime = Get-Content -Raw -LiteralPath $runtimeMarker -Encoding UTF8 | ConvertFrom-Json
        } catch {
            throw "A WorkBuddy Skill has an invalid ownership marker and was preserved: $targetSkill"
        }
        if ($existingRuntime.schema_version -ne 'golden-key-workbuddy-runtime-location-v1') {
            throw "A WorkBuddy Skill has an unrecognized ownership marker and was preserved: $targetSkill"
        }
        $existingSkillVersion = [string]$existingRuntime.package_version
        $incomingSkillVersion = [string]$manifest.distribution.package_version
        if ([string]::IsNullOrWhiteSpace($existingSkillVersion) -or $existingSkillVersion -ne $incomingSkillVersion) {
            throw "Cross-version Skill replacement is not enabled; existing=$existingSkillVersion incoming=$incomingSkillVersion. Existing Skill was preserved: $targetSkill"
        }
        $existingOwnedSkills[$skillName] = $true
        $operation = 'repair'
    }
}

$installParent = Split-Path -Parent $InstallRoot
$staging = Join-Path $installParent ('.staging-' + [Guid]::NewGuid().ToString('N'))
$installBackup = Join-Path $installParent ('.backup-' + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $installParent -Force | Out-Null
New-Item -ItemType Directory -Path $staging | Out-Null
foreach ($entry in $manifest.files) {
    $declaredPath = ([string]$entry.path).Replace('\', '/')
    $destination = Join-Path $staging $declaredPath.Replace('/', [IO.Path]::DirectorySeparatorChar)
    $destinationParent = Split-Path -Parent $destination
    New-Item -ItemType Directory -Path $destinationParent -Force | Out-Null
    Copy-Item -LiteralPath $declaredFiles[$declaredPath] -Destination $destination -Force
}
Copy-Item -LiteralPath $manifestPath -Destination (Join-Path $staging 'BUNDLE-MANIFEST.json') -Force
if ($installRootExists) {
    Move-Item -LiteralPath $InstallRoot -Destination $installBackup
}
try {
    Move-Item -LiteralPath $staging -Destination $InstallRoot
} catch {
    if ($installRootExists -and (Test-Path -LiteralPath $installBackup)) {
        Move-Item -LiteralPath $installBackup -Destination $InstallRoot
    }
    throw
}

foreach ($directory in @('Caches', 'Config', 'Jobs', 'Logs', 'Models', 'Projects', 'Temp')) {
    New-Item -ItemType Directory -Path (Join-Path $DataRoot $directory) -Force | Out-Null
}
New-Item -ItemType Directory -Path $WorkBuddySkillsRoot -Force | Out-Null
$launcherPath = Join-Path $InstallRoot 'golden-key-workbuddy.ps1'
$runtimeRecord = @{
    schema_version = 'golden-key-workbuddy-runtime-location-v1'
    package_version = [string]$manifest.distribution.package_version
    core_tag = [string]$manifest.core.tag
    install_root = $InstallRoot
    data_root = $DataRoot
    launcher = $launcherPath
}
$runtimeJson = $runtimeRecord | ConvertTo-Json -Depth 5

$skillBackups = @{}
foreach ($skillName in $skillNames) {
    $sourceSkill = Join-Path $InstallRoot ("workbuddy-skill\$skillName")
    $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
    if ($existingOwnedSkills.ContainsKey($skillName)) {
        $skillBackup = Join-Path $WorkBuddySkillsRoot ('.backup-' + $skillName + '-' + [Guid]::NewGuid().ToString('N'))
        Move-Item -LiteralPath $targetSkill -Destination $skillBackup
        $skillBackups[$skillName] = $skillBackup
    }
    Copy-Item -LiteralPath $sourceSkill -Destination $targetSkill -Recurse
    Set-Content -LiteralPath (Join-Path $targetSkill 'WORKBUDDY-RUNTIME.json') -Value $runtimeJson -Encoding UTF8
}

$installRecord = @{
    schema_version = 'golden-key-workbuddy-install-v1'
    package_version = [string]$manifest.distribution.package_version
    core = $manifest.core
    install_root = $InstallRoot
    data_root = $DataRoot
    workbuddy_skills_root = $WorkBuddySkillsRoot
    mcp_enabled = $false
    operation = $operation
    source_package = @{
        copy_mode = 'manifest_allowlist'
        extra_files_ignored = $extraFiles
    }
}
$installRecordPath = Join-Path $InstallRoot 'WORKBUDDY-INSTALL.json'
$installRecord | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $installRecordPath -Encoding UTF8

$doctorOutput = & $launcherPath doctor --json 2>&1
$doctorExitCode = $LASTEXITCODE
try {
    $doctorReport = ($doctorOutput -join [Environment]::NewLine) | ConvertFrom-Json
} catch {
    $doctorReport = @{
        status = 'fail'
        provider_calls_attempted = 0
        network_calls_attempted = 0
        errors = @('The post-install doctor did not return valid JSON.')
    }
}
$installRecord['doctor_exit_code'] = $doctorExitCode
$installRecord['doctor'] = $doctorReport
$installRecord | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $installRecordPath -Encoding UTF8
$installRecord['replaced_owned_install'] = $installRootExists
$installRecord['replaced_owned_skills'] = @($skillBackups.Keys | Sort-Object)
$installRecord | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $installRecordPath -Encoding UTF8

if (Test-Path -LiteralPath $installBackup) {
    Remove-Item -LiteralPath $installBackup -Recurse -Force
}
foreach ($skillBackup in $skillBackups.Values) {
    if (Test-Path -LiteralPath $skillBackup) {
        Remove-Item -LiteralPath $skillBackup -Recurse -Force
    }
}
$installRecord | ConvertTo-Json -Depth 8
