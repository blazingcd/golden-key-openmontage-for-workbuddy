# Golden Key OpenMontage for WorkBuddy：首包快速开始

状态：`Pre-Alpha / 首个轻量ZIP构建验证包`

这个 ZIP 使用锁定的 `golden-key-v0.3.21` Callable Core 来验证第一条安装和 WorkBuddy 调用链。
它不是最终 Core 版本，也不代表已经通过普通用户安装验收或真实 Provider 成片验收。

## 使用方式

1. 把 ZIP 解压到任意本地目录。
2. 双击解压目录中的 `安装到WorkBuddy.cmd`。它会校验包完整性、完成注册并自动运行一次离线环境检查。默认写入当前Windows用户的
   `%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy`，可通过参数改到D盘或其他目录。
3. 完全退出并重新打开 WorkBuddy，让它重新发现两个用户级 Skill。
4. 可以先说“我不知道怎么开始做视频”，触发新手引导；也可以直接说一个明确的视频目标，进入生产 Skill。

安装结束和 WorkBuddy 首次调用都会运行只读 `doctor`，检查 Core 合同、4条业务Pipeline、Python、Node和FFmpeg。
检查不会调用真实或付费 Provider，也不会自动下载缺失组件。MCP默认不启用，CLI仍是权威回退。

如果只缺Python包，WorkBuddy会先说明下载内容和保存位置并询问一次。只有用户明确同意后，它才会调用
`runtime prepare --confirm-download`，在所选数据目录的`Runtime/Python`下建立项目自用环境；不会把依赖装进
系统Python。默认数据目录在`%LOCALAPPDATA%`，若安装时把`DataRoot`改到D盘，托管环境也会落在D盘。

Python是运行必需项；FFmpeg在合成和本地媒体处理时必需；Node只在选择Remotion或HyperFrames时需要。
首包不会因为检测到Node缺失就自动安装它，也不会把三套运行时整体塞进ZIP。

面向维护者或需要自定义安装路径的高级用户，仍可直接运行 `install-workbuddy.ps1` 并传入参数。开发仓库中的
`setup.py` 是 WorkBuddy 消费层自己的Python包元数据；普通用户ZIP不携带它，也不需要运行它。

## 路径说明

- ZIP解压位置：任意位置，只用于启动注册。
- 默认程序和数据：当前用户的`%LOCALAPPDATA%`。
- D盘用户可显式传入`-InstallRoot`和`-DataRoot`。
- 注册后不要直接移动已安装目录；如需迁移，应重新执行后续提供的升级/迁移流程。

## 覆盖解压或误删后怎么办

- 可以把新 ZIP 直接覆盖解压到原来的解压文件夹，再双击`安装到WorkBuddy.cmd`。旧包残留文件不会进入正式安装目录。
- 也可以解压到另一个文件夹再运行；它仍会定位并修复同一个正式安装位置，不会因为解压位置不同创建第二份用户数据。
- 如果没有卸载就手动删除了正式程序目录，重新运行一份完整且校验通过的包即可恢复程序和两个Skill。
- 如果只删除了一个项目自有Skill，重复运行也会补回；`Projects`、配置、模型、缓存和输出保留在独立数据目录。
- 如果同名Skill不是本项目创建的，或正式程序目录只剩下无法识别的残片，安装器会停止并保留现场，不会强行覆盖。
- 如果现有安装与当前ZIP版本不同，安装器也会停止，避免旧包静默降级或未经定义的跨版本覆盖。

跨版本降级、完整卸载和版本回滚仍在Pre-Alpha后续任务中；不要把当前“重复注册修复”理解为这些功能已经完成。

## 高级用户手动检查

通常由WorkBuddy完成以下对话和调用。需要手动排查时，可通过已安装的`golden-key-workbuddy.ps1`运行：

```powershell
.\golden-key-workbuddy.ps1 runtime plan --json
.\golden-key-workbuddy.ps1 runtime prepare --confirm-download --json
.\golden-key-workbuddy.ps1 doctor --json
```

第二条命令会访问Python包源下载依赖，因此必须在用户明确同意后运行；它不会调用视频、图像、语音或其他付费Provider。
