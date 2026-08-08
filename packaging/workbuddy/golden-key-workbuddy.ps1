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
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'

# The portable ZIP stays small.  After one explicit user confirmation, the
# complete production environment lives under DataRoot and is exposed only to
# this launcher process.  No machine/user PATH entry is created.
$managedFfmpegBin = Join-Path $dataRoot 'Runtime\FFmpeg\bin'
$managedNodeRoot = Join-Path $dataRoot 'Runtime\Node'
$managedHyperFramesBin = Join-Path $dataRoot 'Runtime\Composition\HyperFrames\node_modules\.bin'
$managedPathEntries = @(
    $managedFfmpegBin,
    $managedNodeRoot,
    $managedHyperFramesBin
) | Where-Object { Test-Path -LiteralPath $_ -PathType Container }
if ($managedPathEntries.Count -gt 0) {
    $existingProcessPath = [Environment]::GetEnvironmentVariable('PATH', 'Process')
    $env:PATH = (($managedPathEntries + @($existingProcessPath)) -join [IO.Path]::PathSeparator)
}
$env:NPM_CONFIG_CACHE = Join-Path $dataRoot 'Caches\npm'
$env:HYPERFRAMES_EXTRACT_CACHE_DIR = Join-Path $dataRoot 'Caches\HyperFrames\ExtractedFrames'
$env:HYPERFRAMES_FONT_CACHE_DIR = Join-Path $dataRoot 'Caches\HyperFrames\Fonts'

$productionRecordPath = Join-Path $dataRoot 'Runtime\WORKBUDDY-PRODUCTION-RUNTIME.json'
if (Test-Path -LiteralPath $productionRecordPath -PathType Leaf) {
    try {
        $productionRecord = Get-Content -Raw -LiteralPath $productionRecordPath -Encoding UTF8 | ConvertFrom-Json
        if ([string]$productionRecord.schema_version -eq 'golden-key-workbuddy-production-runtime-v1') {
            $browserPath = [string]$productionRecord.components.browser.executable
            $browserRoot = [IO.Path]::GetFullPath((Join-Path $dataRoot 'Runtime\Browsers\HyperFrames'))
            $browserCandidate = [IO.Path]::GetFullPath($browserPath)
            $browserPrefix = $browserRoot.TrimEnd('\', '/') + [IO.Path]::DirectorySeparatorChar
            if (
                $browserCandidate.StartsWith($browserPrefix, [StringComparison]::OrdinalIgnoreCase) -and
                (Test-Path -LiteralPath $browserCandidate -PathType Leaf)
            ) {
                $env:HYPERFRAMES_BROWSER_PATH = $browserCandidate
                $env:REMOTION_BROWSER_EXECUTABLE = $browserCandidate
            }
        }
    } catch {
        # `doctor` reports a corrupt or incomplete managed production record.
        # The launcher never searches other folders or trusts an outside path.
    }
}

$credentialStore = Join-Path $dataRoot 'Config\golden-key-provider-credentials.json'
if (Test-Path -LiteralPath $credentialStore -PathType Leaf) {
    if (-not $IsWindows -and $PSVersionTable.PSEdition -eq 'Core') {
        # The current portable package writes Windows DPAPI credentials only.
    } else {
        try {
            $credentialRecord = Get-Content -Raw -LiteralPath $credentialStore -Encoding UTF8 | ConvertFrom-Json
            if ([string]$credentialRecord.schema_version -ne 'golden-key-provider-credentials-v1' -or
                [string]$credentialRecord.protection -ne 'windows_dpapi_current_user') {
                throw 'The local API-key store has an unsupported format.'
            }
            $allowedProviderEnvVars = @(
                'DASHSCOPE_API_KEY', 'DOUBAO_SPEECH_API_KEY', 'VOLC_ACCESSKEY',
                'VOLC_SECRETKEY', 'KLING_API_KEY', 'FAL_KEY', 'FAL_AI_API_KEY',
                'REPLICATE_API_TOKEN'
            )
            foreach ($property in $credentialRecord.credentials.PSObject.Properties) {
                $name = [string]$property.Name
                if ($name -notin $allowedProviderEnvVars) {
                    throw "The local API-key store contains an unsupported variable: $name"
                }
                if (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($name, 'Process'))) {
                    continue
                }
                $secureValue = ConvertTo-SecureString ([string]$property.Value)
                $secretPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureValue)
                try {
                    $plainValue = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($secretPointer)
                    [Environment]::SetEnvironmentVariable($name, $plainValue, 'Process')
                } finally {
                    if ($secretPointer -ne [IntPtr]::Zero) {
                        [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($secretPointer)
                    }
                    $plainValue = $null
                }
            }
        } catch {
            @{
                status = 'fail'
                provider_calls_attempted = 0
                network_calls_attempted = 0
                errors = @('The local API-key store could not be opened by the current Windows user. Run 配置API密钥.cmd again.')
            } | ConvertTo-Json -Depth 4
            exit 1
        }
    }
}

$existingPythonPath = [Environment]::GetEnvironmentVariable('PYTHONPATH', 'Process')
if ([string]::IsNullOrWhiteSpace($existingPythonPath)) {
    $env:PYTHONPATH = $runtimeRoot
} else {
    $env:PYTHONPATH = "$runtimeRoot$([IO.Path]::PathSeparator)$existingPythonPath"
}

$managedRecord = Join-Path $dataRoot 'Runtime\Python\WORKBUDDY-MANAGED-PYTHON.json'
$managedPython = Join-Path $dataRoot 'Runtime\Python\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $managedPython -PathType Leaf)) {
    $managedPython = Join-Path $dataRoot 'Runtime/Python/bin/python'
}
if (
    (Test-Path -LiteralPath $managedRecord -PathType Leaf) -and
    (Test-Path -LiteralPath $managedPython -PathType Leaf)
) {
    Push-Location $runtimeRoot
    try {
        & $managedPython -m golden_key_openmontage_workbuddy @CommandArgs
        $commandExitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    exit $commandExitCode
}

$bundledPython = Join-Path $runtimeRoot 'bootstrap\python\python.exe'
if (Test-Path -LiteralPath $bundledPython -PathType Leaf) {
    Push-Location $runtimeRoot
    try {
        & $bundledPython -m golden_key_openmontage_workbuddy @CommandArgs
        $commandExitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    exit $commandExitCode
}

$python = Get-Command python -ErrorAction SilentlyContinue
if ($null -ne $python) {
    Push-Location $runtimeRoot
    try {
        & $python.Source -m golden_key_openmontage_workbuddy @CommandArgs
        $commandExitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    exit $commandExitCode
}

$launcher = Get-Command py -ErrorAction SilentlyContinue
if ($null -ne $launcher) {
    Push-Location $runtimeRoot
    try {
        & $launcher.Source -3 -m golden_key_openmontage_workbuddy @CommandArgs
        $commandExitCode = $LASTEXITCODE
    } finally {
        Pop-Location
    }
    exit $commandExitCode
}

@{
    status = 'fail'
    provider_calls_attempted = 0
    network_calls_attempted = 0
    errors = @('Python 3.10 or newer was not found. Run the package doctor after installing Python, or choose a later package that includes a managed runtime.')
} | ConvertTo-Json -Depth 4
exit 1
