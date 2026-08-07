[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$packageRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$launcher = Join-Path $packageRoot 'golden-key-workbuddy.ps1'
$installRecordPath = Join-Path $packageRoot 'WORKBUDDY-INSTALL.json'

if (-not (Test-Path -LiteralPath $launcher -PathType Leaf)) {
    throw 'golden-key-workbuddy.ps1 is missing. Use a complete package.'
}
if (-not ($env:OS -eq 'Windows_NT')) {
    throw 'The current API-key wizard requires Windows current-user DPAPI.'
}

$dataRoot = Join-Path $env:LOCALAPPDATA 'GoldenKeyOpenMontageForWorkBuddy\Data'
if (Test-Path -LiteralPath $installRecordPath -PathType Leaf) {
    $installRecord = Get-Content -Raw -LiteralPath $installRecordPath -Encoding UTF8 | ConvertFrom-Json
    if (-not [string]::IsNullOrWhiteSpace([string]$installRecord.data_root)) {
        $dataRoot = [string]$installRecord.data_root
    }
}

$guideOutput = & $launcher config guide --data-root $dataRoot --json 2>&1
if ($LASTEXITCODE -ne 0) {
    throw ('Cannot read the Provider setup guide: ' + ($guideOutput -join [Environment]::NewLine))
}
$guide = ($guideOutput -join [Environment]::NewLine) | ConvertFrom-Json
if ($guide.status -ne 'pass') {
    throw 'The Provider setup guide is not available.'
}

Write-Host ''
Write-Host 'Golden Key OpenMontage API 密钥配置' -ForegroundColor Cyan
Write-Host '密钥只在本窗口隐藏输入；不要把密钥粘贴到 WorkBuddy 聊天。'
Write-Host '保存密钥不会联网、不会测试余额，也不会调用付费 Provider。'
Write-Host ''

$providers = @($guide.providers)
for ($index = 0; $index -lt $providers.Count; $index++) {
    $provider = $providers[$index]
    $pathLabel = if ($provider.access_path -eq 'direct_vendor_api') { '厂商直连' } else { '第三方网关' }
    $capabilities = @($provider.capabilities) -join ', '
    Write-Host ("[{0}] {1} | {2} | {3} | {4}" -f ($index + 1), $provider.service, $pathLabel, $capabilities, $provider.credential_state)
}

Write-Host ''
$selectionText = Read-Host '输入要配置的编号，可用逗号分隔；直接回车取消'
if ([string]::IsNullOrWhiteSpace($selectionText)) {
    Write-Host '未做更改。'
    exit 0
}

$selectedIndexes = @()
foreach ($part in ($selectionText -split '[,，\s]+')) {
    if ([string]::IsNullOrWhiteSpace($part)) { continue }
    $number = 0
    if (-not [int]::TryParse($part, [ref]$number) -or $number -lt 1 -or $number -gt $providers.Count) {
        throw "无效编号：$part"
    }
    $selectedIndexes += ($number - 1)
}
$selectedIndexes = @($selectedIndexes | Select-Object -Unique)

$storePath = [string]$guide.credential_store.path
$storeDirectory = Split-Path -Parent $storePath
New-Item -ItemType Directory -Force -Path $storeDirectory | Out-Null
$credentials = [ordered]@{}
if (Test-Path -LiteralPath $storePath -PathType Leaf) {
    $existing = Get-Content -Raw -LiteralPath $storePath -Encoding UTF8 | ConvertFrom-Json
    if ([string]$existing.schema_version -ne 'golden-key-provider-credentials-v1' -or
        [string]$existing.protection -ne 'windows_dpapi_current_user') {
        throw '现有API密钥文件格式无法识别，已保留原文件。'
    }
    foreach ($property in $existing.credentials.PSObject.Properties) {
        $credentials[[string]$property.Name] = [string]$property.Value
    }
}

foreach ($selectedIndex in $selectedIndexes) {
    $provider = $providers[$selectedIndex]
    $options = @($provider.credential_options)
    $optionIndex = 0
    if ($options.Count -gt 1) {
        Write-Host ''
        Write-Host ("{0} 有多个接入方式：" -f $provider.service)
        for ($index = 0; $index -lt $options.Count; $index++) {
            Write-Host ("  [{0}] {1}" -f ($index + 1), (@($options[$index]) -join ' + '))
        }
        $optionText = Read-Host '选择接入方式编号'
        $optionNumber = 0
        if (-not [int]::TryParse($optionText, [ref]$optionNumber) -or $optionNumber -lt 1 -or $optionNumber -gt $options.Count) {
            throw "无效接入方式：$optionText"
        }
        $optionIndex = $optionNumber - 1
    }

    foreach ($envName in @($options[$optionIndex])) {
        if (@($provider.present_env_vars) -contains $envName) {
            $replace = Read-Host "$envName 已存在于当前环境，是否写入或替换本地加密副本？[y/N]"
            if ($replace -notmatch '^[yY]$') { continue }
        }
        $secureValue = Read-Host "请输入 $envName" -AsSecureString
        $secretPointer = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureValue)
        try {
            $plainValue = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($secretPointer)
            if ([string]::IsNullOrWhiteSpace($plainValue) -or $plainValue.Contains("`r") -or $plainValue.Contains("`n")) {
                throw "$envName 不能为空或包含换行。"
            }
            $credentials[$envName] = ConvertFrom-SecureString $secureValue
        } finally {
            if ($secretPointer -ne [IntPtr]::Zero) {
                [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($secretPointer)
            }
            $plainValue = $null
        }
    }
}

$record = [ordered]@{
    schema_version = 'golden-key-provider-credentials-v1'
    protection = 'windows_dpapi_current_user'
    credentials = $credentials
}
$temporaryPath = Join-Path $storeDirectory ('.provider-credentials-' + [Guid]::NewGuid().ToString('N') + '.tmp')
try {
    $record | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $temporaryPath -Encoding UTF8
    Move-Item -LiteralPath $temporaryPath -Destination $storePath -Force
    $currentSid = [Security.Principal.WindowsIdentity]::GetCurrent().User.Value
    & icacls.exe $storePath '/inheritance:r' '/grant:r' ("*{0}:(F)" -f $currentSid) | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw '无法限制API密钥文件权限。'
    }
} finally {
    if (Test-Path -LiteralPath $temporaryPath) {
        Remove-Item -LiteralPath $temporaryPath -Force
    }
}

Write-Host ''
Write-Host 'API密钥已使用当前Windows用户DPAPI加密保存。' -ForegroundColor Green
Write-Host "位置：$storePath"
Write-Host '当前仅确认“已录入”，尚未联网验证账号权限、余额或模型可用性。'
Write-Host '回到WorkBuddy后告诉它“API密钥配置完成”，让它重新检查。'
