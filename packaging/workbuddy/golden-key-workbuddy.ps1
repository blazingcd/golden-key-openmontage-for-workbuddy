[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$CommandArgs
)

$ErrorActionPreference = 'Stop'
$runtimeRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$installRecordPath = Join-Path $runtimeRoot 'WORKBUDDY-INSTALL.json'
$dataRoot = $null

if (Test-Path -LiteralPath $installRecordPath -PathType Leaf) {
    $installRecord = Get-Content -Raw -LiteralPath $installRecordPath -Encoding UTF8 | ConvertFrom-Json
    $dataRoot = [string]$installRecord.data_root
}
if ([string]::IsNullOrWhiteSpace($dataRoot)) {
    $dataRoot = Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\Data'
}

$env:OPENMONTAGE_WORKBUDDY_ROOT = $runtimeRoot
$env:OPENMONTAGE_WORKBUDDY_DATA_ROOT = $dataRoot
$existingPythonPath = [Environment]::GetEnvironmentVariable('PYTHONPATH', 'Process')
if ([string]::IsNullOrWhiteSpace($existingPythonPath)) {
    $env:PYTHONPATH = $runtimeRoot
} else {
    $env:PYTHONPATH = "$runtimeRoot$([IO.Path]::PathSeparator)$existingPythonPath"
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($null -ne $python) {
    & $python.Source -m golden_key_openmontage_workbuddy @CommandArgs
    exit $LASTEXITCODE
}

$launcher = Get-Command py -ErrorAction SilentlyContinue
if ($null -ne $launcher) {
    & $launcher.Source -3 -m golden_key_openmontage_workbuddy @CommandArgs
    exit $LASTEXITCODE
}

@{
    status = 'fail'
    provider_calls_attempted = 0
    network_calls_attempted = 0
    errors = @('Python 3.10 or newer was not found. Run the package doctor after installing Python, or choose a later package that includes a managed runtime.')
} | ConvertTo-Json -Depth 4
exit 1
