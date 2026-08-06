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

foreach ($entry in $manifest.files) {
    $relative = ([string]$entry.path).Replace('/', [IO.Path]::DirectorySeparatorChar)
    $candidate = Join-Path $sourceRoot $relative
    if (-not (Test-Path -LiteralPath $candidate -PathType Leaf)) {
        throw "Package file is missing: $($entry.path)"
    }
    $actual = Get-FileSha256 -Path $candidate
    if ($actual -ne ([string]$entry.sha256).ToLowerInvariant()) {
        throw "Package file hash mismatch: $($entry.path)"
    }
}

$skillNames = @('golden-key-openmontage', 'golden-key-openmontage-onboarding')
foreach ($skillName in $skillNames) {
    $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
    if (Test-Path -LiteralPath $targetSkill) {
        throw "WorkBuddy Skill already exists and was not overwritten: $targetSkill"
    }
}
if (Test-Path -LiteralPath $InstallRoot) {
    throw "InstallRoot already exists and was not overwritten: $InstallRoot"
}

$installParent = Split-Path -Parent $InstallRoot
$staging = Join-Path $installParent ('.staging-' + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $installParent -Force | Out-Null
New-Item -ItemType Directory -Path $staging | Out-Null
foreach ($item in Get-ChildItem -LiteralPath $sourceRoot -Force) {
    Copy-Item -LiteralPath $item.FullName -Destination $staging -Recurse -Force
}
Move-Item -LiteralPath $staging -Destination $InstallRoot

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

foreach ($skillName in $skillNames) {
    $sourceSkill = Join-Path $InstallRoot ("workbuddy-skill\$skillName")
    $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
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
$installRecord | ConvertTo-Json -Depth 8
