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

面向维护者或需要自定义安装路径的高级用户，仍可直接运行 `install-workbuddy.ps1` 并传入参数。开发仓库中的
`setup.py` 是 WorkBuddy 消费层自己的Python包元数据；普通用户ZIP不携带它，也不需要运行它。

## 路径说明

- ZIP解压位置：任意位置，只用于启动注册。
- 默认程序和数据：当前用户的`%LOCALAPPDATA%`。
- D盘用户可显式传入`-InstallRoot`和`-DataRoot`。
- 注册后不要直接移动已安装目录；如需迁移，应重新执行后续提供的升级/迁移流程。
