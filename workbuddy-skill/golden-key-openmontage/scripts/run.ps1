param(
    [Parameter(ValueFromPipeline = $true)]
    [AllowEmptyString()]
    [string]$UserMessage
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$packageRoot = <installer:package_root>
$python = <installer:private_python>
$dataRoot = <installer:data_root>
$expectedActivePointerSha256 = '<installer:active_pointer_sha256>'
$receiptPath = <installer:receipt_path>
$previousLocation = $null
$receiptDirectory = $null
$failureDiagnosticPath = $null
$receiptTemporaryPath = $null
$stage = 'startup'
$exitCode = 64
$utf8 = [System.Text.UTF8Encoding]::new($false)

function Write-FailureDiagnostic {
    param(
        [int]$Code,
        [string]$Phase,
        [string]$ErrorText
    )

    if ($null -eq $failureDiagnosticPath -or $null -eq $receiptDirectory) {
        return
    }
    $temporaryPath = $null
    try {
        [void][System.IO.Directory]::CreateDirectory($receiptDirectory)
        $temporaryPath = Join-Path -Path $receiptDirectory -ChildPath ('.latest-launcher-failure.' + [guid]::NewGuid().ToString('N') + '.tmp')
        $diagnostic = [ordered]@{
            schema_version = 'golden-key-workbuddy-failure-diagnostic-v1'
            exit_code = $Code
            stage = $Phase
            error = $ErrorText
        }
        $payload = $diagnostic | ConvertTo-Json -Depth 2
        [System.IO.File]::WriteAllText($temporaryPath, $payload + [Environment]::NewLine, $utf8)
        Move-Item -LiteralPath $temporaryPath -Destination $failureDiagnosticPath -Force
        $temporaryPath = $null
    }
    catch {
        [Console]::Error.Write(($_.Exception.Message + [Environment]::NewLine))
    }
    finally {
        if ($null -ne $temporaryPath -and (Test-Path -LiteralPath $temporaryPath -PathType Leaf)) {
            Remove-Item -LiteralPath $temporaryPath -Force
        }
    }
}

try {
    $stage = 'initialize'
    $previousLocation = Get-Location
    $receiptDirectory = [System.IO.Path]::GetDirectoryName($receiptPath)
    if ([string]::IsNullOrWhiteSpace($receiptDirectory)) {
        throw 'WORKBUDDY_RECEIPT_PATH_INVALID'
    }
    $failureDiagnosticPath = Join-Path -Path $receiptDirectory -ChildPath 'latest-launcher-failure.json'

    $stage = 'preflight'
    if ([string]::IsNullOrWhiteSpace($UserMessage)) {
        throw 'WORKBUDDY_SKILL_INVALID'
    }
    if ($expectedActivePointerSha256 -ne 'MISSING') {
        $activePointerPath = Join-Path -Path $dataRoot -ChildPath 'State\PackageRegistration\v1\active.json'
        if (-not (Test-Path -LiteralPath $activePointerPath -PathType Leaf)) {
            throw 'WORKBUDDY_SKILL_STALE'
        }
        $activePointerSha256 = (Get-FileHash -LiteralPath $activePointerPath -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($activePointerSha256 -ne $expectedActivePointerSha256) {
            throw 'WORKBUDDY_SKILL_STALE'
        }
    }

    Set-Location -LiteralPath $packageRoot
    [Console]::OutputEncoding = $utf8
    $OutputEncoding = $utf8
    $stage = 'invoke'
    [void][System.IO.Directory]::CreateDirectory($receiptDirectory)
    $receiptTemporaryPath = Join-Path -Path $receiptDirectory -ChildPath ('.latest-launcher-receipt.' + [guid]::NewGuid().ToString('N') + '.tmp')
    $receiptText = $UserMessage | & $python -I -m golden_key_openmontage_workbuddy.user_entry | Out-String
    $exitCode = $LASTEXITCODE
    if ($exitCode -eq 0) {
        if ([string]::IsNullOrWhiteSpace($receiptText)) {
            throw 'WORKBUDDY_RECEIPT_MISSING'
        }
        [System.IO.File]::WriteAllText($receiptTemporaryPath, $receiptText, $utf8)
        # Same-directory rename keeps the visible receipt complete or unchanged.
        Move-Item -LiteralPath $receiptTemporaryPath -Destination $receiptPath -Force
        $receiptTemporaryPath = $null
        if (Test-Path -LiteralPath $failureDiagnosticPath -PathType Leaf) {
            Remove-Item -LiteralPath $failureDiagnosticPath -Force
        }
        [Console]::Out.Write($receiptText)
    }
    else {
        $stage = 'native_exit'
        [void](Write-FailureDiagnostic -Code $exitCode -Phase $stage -ErrorText ('canonical entry returned exit code ' + $exitCode))
        exit $exitCode
    }
}
catch {
    $failureExitCode = if ($exitCode -eq 0) { 64 } else { $exitCode }
    $errorText = $_.Exception.Message
    if (-not [string]::IsNullOrEmpty($UserMessage)) {
        $errorText = $errorText.Replace($UserMessage, '[user message omitted]')
    }
    [void](Write-FailureDiagnostic -Code $failureExitCode -Phase $stage -ErrorText $errorText)
    [Console]::Error.Write("WORKBUDDY_SKILL_INVALID`n")
    exit $failureExitCode
}
finally {
    if ($null -ne $receiptTemporaryPath -and (Test-Path -LiteralPath $receiptTemporaryPath -PathType Leaf)) {
        Remove-Item -LiteralPath $receiptTemporaryPath -Force
    }
    if ($null -ne $previousLocation) {
        Set-Location -LiteralPath $previousLocation
    }
}
