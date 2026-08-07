[CmdletBinding()]
param(
    [string]$InstallRoot,
    [string]$DataRoot = (Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\Data'),
    [string]$WorkBuddySkillsRoot = (Join-Path $env:USERPROFILE '.workbuddy\skills')
)

$ErrorActionPreference = 'Stop'

# WorkBuddy and CI both launch this script with redirected streams.  Convert
# every otherwise-unhandled terminating error into a native stderr message so
# callers receive the reason together with a deterministic non-zero exit.
trap {
    [Console]::Error.WriteLine($_.Exception.Message)
    exit 1
}

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

function Compare-PackageVersion {
    param(
        [Parameter(Mandatory = $true)][string]$Left,
        [Parameter(Mandatory = $true)][string]$Right
    )

    $pattern = '^(\d+)\.(\d+)\.(\d+)(?:-([0-9A-Za-z.-]+))?$'
    $leftMatch = [regex]::Match($Left, $pattern)
    $rightMatch = [regex]::Match($Right, $pattern)
    if (-not $leftMatch.Success -or -not $rightMatch.Success) {
        throw "Unsupported package version comparison: left=$Left right=$Right"
    }
    foreach ($index in 1..3) {
        $leftNumber = [int64]$leftMatch.Groups[$index].Value
        $rightNumber = [int64]$rightMatch.Groups[$index].Value
        if ($leftNumber -lt $rightNumber) { return -1 }
        if ($leftNumber -gt $rightNumber) { return 1 }
    }
    $leftPrerelease = $leftMatch.Groups[4].Value
    $rightPrerelease = $rightMatch.Groups[4].Value
    if ($leftPrerelease -eq $rightPrerelease) { return 0 }
    if ([string]::IsNullOrWhiteSpace($leftPrerelease)) { return 1 }
    if ([string]::IsNullOrWhiteSpace($rightPrerelease)) { return -1 }
    $leftParts = @($leftPrerelease.Split('.'))
    $rightParts = @($rightPrerelease.Split('.'))
    $count = [Math]::Max($leftParts.Count, $rightParts.Count)
    for ($index = 0; $index -lt $count; $index++) {
        if ($index -ge $leftParts.Count) { return -1 }
        if ($index -ge $rightParts.Count) { return 1 }
        $leftNumeric = $leftParts[$index] -match '^\d+$'
        $rightNumeric = $rightParts[$index] -match '^\d+$'
        if ($leftNumeric -and $rightNumeric) {
            $leftNumber = [int64]$leftParts[$index]
            $rightNumber = [int64]$rightParts[$index]
            if ($leftNumber -lt $rightNumber) { return -1 }
            if ($leftNumber -gt $rightNumber) { return 1 }
        } elseif ($leftNumeric -and -not $rightNumeric) {
            return -1
        } elseif (-not $leftNumeric -and $rightNumeric) {
            return 1
        } else {
            $comparison = [string]::CompareOrdinal($leftParts[$index], $rightParts[$index])
            if ($comparison -lt 0) { return -1 }
            if ($comparison -gt 0) { return 1 }
        }
    }
    return 0
}

function Test-PathEqual {
    param(
        [Parameter(Mandatory = $true)][string]$Left,
        [Parameter(Mandatory = $true)][string]$Right
    )

    $leftFull = [IO.Path]::GetFullPath($Left).TrimEnd('\', '/')
    $rightFull = [IO.Path]::GetFullPath($Right).TrimEnd('\', '/')
    return [string]::Equals($leftFull, $rightFull, [StringComparison]::OrdinalIgnoreCase)
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
$incomingVersion = [string]$manifest.distribution.package_version
if ([string]::IsNullOrWhiteSpace($InstallRoot)) {
    $InstallRoot = Join-Path $env:LOCALAPPDATA "GoldenKeyOpenMontageForWorkBuddy\App\$incomingVersion"
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
$previousInstallRoot = $null
$previousVersion = $null
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
    if ([string]::IsNullOrWhiteSpace($existingVersion)) {
        throw "InstallRoot package version is missing and was preserved: $InstallRoot"
    }
    $versionComparison = Compare-PackageVersion -Left $existingVersion -Right $incomingVersion
    if ($versionComparison -gt 0) {
        throw "Package downgrade is not allowed; existing=$existingVersion incoming=$incomingVersion. Existing install was preserved."
    }
    if ($versionComparison -lt 0) {
        $operation = 'upgrade'
        $previousInstallRoot = $InstallRoot
        $previousVersion = $existingVersion
    } else {
        $operation = 'repair'
    }
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
        $existingSkillDataRoot = [string]$existingRuntime.data_root
        if ([string]::IsNullOrWhiteSpace($existingSkillDataRoot) -or
            -not (Test-PathEqual -Left $existingSkillDataRoot -Right $DataRoot)) {
            throw "DataRoot does not match the existing WorkBuddy Skill and was preserved: $targetSkill"
        }
        $existingSkillVersion = [string]$existingRuntime.package_version
        if ([string]::IsNullOrWhiteSpace($existingSkillVersion)) {
            throw "A WorkBuddy Skill package version is missing and was preserved: $targetSkill"
        }
        $skillVersionComparison = Compare-PackageVersion -Left $existingSkillVersion -Right $incomingVersion
        if ($skillVersionComparison -gt 0) {
            throw "Package downgrade is not allowed; existing Skill=$existingSkillVersion incoming=$incomingVersion. Existing Skill was preserved: $targetSkill"
        }
        if ($skillVersionComparison -lt 0) {
            $skillInstallRoot = [string]$existingRuntime.install_root
            if ($previousVersion -and $previousVersion -ne $existingSkillVersion) {
                throw "Existing WorkBuddy installation versions are inconsistent and were preserved."
            }
            if ($previousInstallRoot -and
                -not (Test-PathEqual -Left $previousInstallRoot -Right $skillInstallRoot)) {
                throw "Existing WorkBuddy installation paths are inconsistent and were preserved."
            }
            $previousVersion = $existingSkillVersion
            $previousInstallRoot = $skillInstallRoot
            $operation = 'upgrade'
        } elseif ($operation -eq 'fresh_install') {
            $operation = 'repair'
        }
        $existingOwnedSkills[$skillName] = $true
    }
}

if ($previousInstallRoot -and
    -not (Test-PathEqual -Left $previousInstallRoot -Right $InstallRoot) -and
    (Test-Path -LiteralPath $previousInstallRoot)) {
    $previousRecordPath = Join-Path $previousInstallRoot 'WORKBUDDY-INSTALL.json'
    if (-not (Test-Path -LiteralPath $previousRecordPath -PathType Leaf)) {
        throw "Previous install is not owned and was preserved: $previousInstallRoot"
    }
    try {
        $previousRecord = Get-Content -Raw -LiteralPath $previousRecordPath -Encoding UTF8 | ConvertFrom-Json
    } catch {
        throw "Previous install ownership record is invalid and was preserved: $previousInstallRoot"
    }
    if ($previousRecord.schema_version -ne 'golden-key-workbuddy-install-v1' -or
        [string]$previousRecord.package_version -ne $previousVersion) {
        throw "Previous install ownership does not match its Skill records and was preserved: $previousInstallRoot"
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

$skillBackups = @{}
$installRecord = $null
try {
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
    if ($operation -eq 'upgrade') {
        $installRecord['previous_install'] = @{
            install_root = $previousInstallRoot
            package_version = $previousVersion
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
    $doctorSucceeded = ($doctorExitCode -in @(0, 1)) -and ($doctorReport.status -in @('pass', 'degraded'))
    if (-not $doctorSucceeded) {
        throw 'Post-install validation failed; previous installation was restored.'
    }
    $installRecord['doctor_exit_code'] = $doctorExitCode
    $installRecord['doctor'] = $doctorReport
    $installRecord['replaced_owned_install'] = $installRootExists
    $installRecord['replaced_owned_skills'] = @($skillBackups.Keys | Sort-Object)
    $installRecord | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $installRecordPath -Encoding UTF8
} catch {
    $failure = $_
    foreach ($skillName in $skillNames) {
        $targetSkill = Join-Path $WorkBuddySkillsRoot $skillName
        if (Test-Path -LiteralPath $targetSkill) {
            Remove-Item -LiteralPath $targetSkill -Recurse -Force
        }
        if ($skillBackups.ContainsKey($skillName) -and (Test-Path -LiteralPath $skillBackups[$skillName])) {
            Move-Item -LiteralPath $skillBackups[$skillName] -Destination $targetSkill
        }
    }
    if (Test-Path -LiteralPath $InstallRoot) {
        Remove-Item -LiteralPath $InstallRoot -Recurse -Force
    }
    if ($installRootExists -and (Test-Path -LiteralPath $installBackup)) {
        Move-Item -LiteralPath $installBackup -Destination $InstallRoot
    }
    # Emit the rollback result through the native stderr stream.  An unhandled
    # PowerShell error record can lose its text when the installer is launched
    # through a long-running redirected test or Agent host, even though the
    # process correctly exits non-zero and the rollback succeeds.
    [Console]::Error.WriteLine($failure.Exception.Message)
    exit 1
}

if (Test-Path -LiteralPath $installBackup) {
    Remove-Item -LiteralPath $installBackup -Recurse -Force
}
foreach ($skillBackup in $skillBackups.Values) {
    if (Test-Path -LiteralPath $skillBackup) {
        Remove-Item -LiteralPath $skillBackup -Recurse -Force
    }
}
if ($operation -eq 'upgrade' -and
    $previousInstallRoot -and
    -not (Test-PathEqual -Left $previousInstallRoot -Right $InstallRoot) -and
    (Test-Path -LiteralPath $previousInstallRoot)) {
    Remove-Item -LiteralPath $previousInstallRoot -Recurse -Force
}
$installRecord | ConvertTo-Json -Depth 8
