param(
    [Parameter(ValueFromPipeline = $true)]
    [AllowEmptyString()]
    [string]$UserMessage
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$packageRoot = <installer:package_root>
$python = <installer:private_python>
$previousLocation = Get-Location

try {
    if ([string]::IsNullOrWhiteSpace($UserMessage)) {
        throw 'WORKBUDDY_SKILL_INVALID'
    }
    Set-Location -LiteralPath $packageRoot
    $utf8 = [System.Text.UTF8Encoding]::new($false)
    [Console]::OutputEncoding = $utf8
    $OutputEncoding = $utf8
    # WorkBuddy blocks Process APIs but permits a bundled script's direct stamped entry.
    $UserMessage | & $python -I -m golden_key_openmontage_workbuddy.user_entry
    # A successful script must return normally so WorkBuddy can relay the receipt output.
    if ($LASTEXITCODE -ne 0) {
        exit $LASTEXITCODE
    }
}
catch {
    [Console]::Error.Write("WORKBUDDY_SKILL_INVALID`n")
    exit 64
}
finally {
    Set-Location -LiteralPath $previousLocation
}
