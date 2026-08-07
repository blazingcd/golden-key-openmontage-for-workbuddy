[CmdletBinding()]
param(
    [string]$InstallRoot,
    [string]$DataRoot = (Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\Data'),
    [string]$WorkBuddySkillsRoot = (Join-Path $env:USERPROFILE '.workbuddy\skills')
)

$ErrorActionPreference = 'Stop'
$installer = Join-Path $PSScriptRoot 'install-workbuddy.ps1'
$manifestPath = Join-Path $PSScriptRoot 'BUNDLE-MANIFEST.json'
if ([string]::IsNullOrWhiteSpace($InstallRoot)) {
    if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
        throw 'BUNDLE-MANIFEST.json is missing. Extract the complete ZIP before registration.'
    }
    $manifest = Get-Content -Raw -LiteralPath $manifestPath -Encoding UTF8 | ConvertFrom-Json
    $packageVersion = [string]$manifest.distribution.package_version
    $InstallRoot = Join-Path $env:LOCALAPPDATA "GoldenKeyOpenMontageForWorkBuddy\App\$packageVersion"
}

function ConvertFrom-Utf8Base64([string]$Value) {
    return [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($Value))
}

try {
    Write-Host (ConvertFrom-Utf8Base64 '5q2j5Zyo5qCh6aqM5bm25a6J6KOF5YiwIFdvcmtCdWRkee+8jOivt+eojeWAmS4uLg==')
    & $installer -InstallRoot $InstallRoot -DataRoot $DataRoot -WorkBuddySkillsRoot $WorkBuddySkillsRoot | Out-Null
    $recordPath = Join-Path $InstallRoot 'WORKBUDDY-INSTALL.json'
    $record = Get-Content -Raw -LiteralPath $recordPath -Encoding UTF8 | ConvertFrom-Json
    Write-Host ''
    Write-Host (ConvertFrom-Utf8Base64 '5a6J6KOF5rOo5YaM5a6M5oiQ44CC6K+35a6M5YWo6YCA5Ye65bm26YeN5paw5omT5byAIFdvcmtCdWRkeeOAgg==')
    Write-Host ((ConvertFrom-Utf8Base64 '546v5aKD5qOA5p+l77yaezB9') -f $record.doctor.status)
    if ($record.doctor.status -ne 'pass') {
        Write-Host (ConvertFrom-Utf8Base64 '546v5aKD5bCa5pyq5a6M5YWo5bCx57uq77yb5omT5byAIFdvcmtCdWRkeSDlkI7kvJror7TmmI7nvLrlpLHpobnnm67jgII=')
    }
    exit 0
} catch {
    Write-Error $_
    exit 1
}
