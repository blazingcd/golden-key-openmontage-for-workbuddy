# WorkBuddy本地存储策略

状态：`W4 USER DEFAULT CORRECTED`

日期：2026-08-06

## 普通用户默认值

Windows产品默认使用当前用户的标准目录，不要求D盘：

```text
%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy\
├── App\<package-version>\  # 稳定程序目录和Callable Core
└── Data\
    ├── Projects\
    ├── Caches\
    ├── Config\
    ├── Models\
    ├── Temp\
    ├── Logs\
    └── Jobs\
```

`install-workbuddy.ps1`允许通过`-InstallRoot`和`-DataRoot`改到D盘、其他磁盘或企业规定位置。
注册后的`WORKBUDDY-RUNTIME.json`记录实际路径，Skill不得硬编码C盘或D盘，也不得扫描磁盘猜测安装位置。

## 当前开发机覆盖

本项目开发、构建、缓存和测试继续使用`D:\WorkBuddyData`，避免非系统工程文件占用本机C盘：

- Python虚拟环境：`D:\WorkBuddyData\Dev\venvs\`；
- pip/Release缓存：`D:\WorkBuddyData\Caches\`；
- pytest、构建、解压和安装烟测：`D:\WorkBuddyData\Temp\`。

这只是维护者机器策略，不进入普通用户默认值。

## 数据与安全

- `.env`和Provider凭据不得进入Git、ZIP、报告、测试夹具或普通日志。
- `Projects`、`Config`、`Models`、`Temp`、`Logs`和`Jobs`不属于Core同步范围。
- 缓存和临时文件可重建；用户项目、Artifact、配置、模型和最终输出不得被升级或卸载默认删除。
- `Jobs`继续保存消费方任务状态；跨项目并发1、运行超时只观察不强杀、失败不自动重试。
- 首包安装器不自动下载运行时或Provider组件；环境发现和后续安装授权分开。

本策略不代表W4普通用户安装验收或`OFFLINE ADAPTER READY`已经通过。
