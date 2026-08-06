# W4轻量ZIP交付决策

决策编号：`PKG-001`

状态：`W4 FIRST VERTICAL SLICE ACTIVE`

记录日期：2026-08-06

## 决策

首个Windows交付物采用轻量`portable ZIP + PowerShell注册脚本`，不是Setup.exe、MSI或独立桌面软件。

- ZIP可解压到任意本地目录。
- 普通用户双击`安装到WorkBuddy.cmd`；它调用本地PowerShell注册脚本，校验包完整性、复制到稳定的用户级安装目录、建立数据目录，并把
  `golden-key-openmontage`和`golden-key-openmontage-onboarding`两个Skill注册到当前用户的WorkBuddy。
- 注册结束立即运行一次只读`doctor`并将结果写入`WORKBUDDY-INSTALL.json`；WorkBuddy首次调用仍会复核。
- 注册后的Skill读取同目录`WORKBUDDY-RUNTIME.json`，通过稳定`launcher`定位Callable Core；不要求用户
  自己寻找仓库，也不扫描磁盘猜路径。
- MCP保持可选且默认关闭；CLI/launcher是首包权威入口。
- 开发仓库保留消费方自有`setup.py`供测试和Python包元数据使用；普通用户ZIP明确排除该文件，避免让用户误以为
  需要执行传统Python源码安装，也避免与Core导出边界混淆。

## v0.3.21临时基线声明

首包完整携带锁定的`golden-key-v0.3.21`、1566个managed文件和
`golden-key-workbuddy-callable-core-v1`合同，只用于建立并验证第一个安装/注册/调用包。

由于Golden Key Core正在进行较大方向调整，本版本不是最终Core，也不得暗示后续正式发行仍以v0.3.21为准。
Core更新必须等待新的不可变Release/ZIP/SHA/lock，再执行独立同步、回归、W0和包升级，不拉取Core `main`。

## 环境策略

首包不把Python、Node、FFmpeg、GPU模型或Provider SDK二进制整体塞进ZIP。WorkBuddy首次触发Skill时：

1. 先运行只读`doctor`，检查Core身份、四Pipeline、Python版本和必需Python包、Node、FFmpeg；
2. 再运行只读`config inspect`，只报告Tool Registry支持的生产Provider配置引用；
3. 不自动下载、不读取或输出密钥值、不调用真实/付费Provider；
4. 缺项时标记为degraded并给出下一步。后续W4再决定经用户确认创建受控Python环境或下载可选组件的方式。

## 默认路径与覆盖

- 普通Windows用户默认程序/数据位置：`%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy`。
- WorkBuddy Skill默认注册位置：`%USERPROFILE%\.workbuddy\skills`。
- 用户可用参数把程序和数据改到D盘或其他位置；本项目开发机继续使用`D:\WorkBuddyData`。
- ZIP解压位置不是稳定运行位置；完成注册后由安装记录定位正式安装目录。

## 尚未通过

- 全新普通Windows环境的完整Python依赖准备、升级、卸载和回滚；
- 真实WorkBuddy普通用户自然语言触发与Human Checkpoint全链验收；
- 真实/付费Provider成片；
- `OFFLINE ADAPTER READY`。
