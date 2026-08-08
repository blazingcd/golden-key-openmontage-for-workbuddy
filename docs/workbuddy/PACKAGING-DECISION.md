# W4轻量ZIP交付决策

决策编号：`PKG-001`

状态：`W4 UPGRADE / ROLLBACK / UNINSTALL SLICE ACTIVE`

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

首包不把Python、Node、FFmpeg、浏览器、GPU模型或Provider SDK二进制整体塞进ZIP。WorkBuddy首次触发Skill时：

1. 先运行只读`doctor`，检查Core身份、四Pipeline、Python版本和必需Python包、Node、FFmpeg；
2. 再运行只读`config inspect`，只报告Tool Registry支持的生产Provider配置引用；
3. 不自动下载、不读取或输出密钥值、不调用真实/付费Provider；
4. 完整视频制作环境未就绪时先运行只读`runtime plan`；向用户说明下载、`<data_root>/Runtime`存储位置、FFmpeg
   GPLv3和Remotion许可条件后，只询问一次。只有用户明确同意，才执行`runtime prepare --confirm-download`。
5. 标准环境同时准备Python依赖、固定hash的FFmpeg与Node、锁定依赖的Remotion与HyperFrames，以及固定版本的
   托管浏览器。缓存只写入`<data_root>/Caches`，不修改系统Python或系统PATH，不要求管理员权限。
6. 安装阶段不要求普通用户理解或选择合成引擎；两者准备完成后，由WorkBuddy在具体视频方案中用普通语言说明并推荐，
   再遵守Core的提案批准合同。大型本地生成模型和在线Provider继续按目标单独配置、按需准备。
7. 组件目录必须带本项目所有权记录；下载资产、包锁和浏览器可执行文件必须通过固定hash或本地记录校验。重复执行
   幂等复用；未知目录或所有权漂移一律拒绝覆盖。

## 默认路径与覆盖

- 普通Windows用户默认程序/数据位置：`%LOCALAPPDATA%\GoldenKeyOpenMontageForWorkBuddy`。
- WorkBuddy Skill默认注册位置：`%USERPROFILE%\.workbuddy\skills`。
- 用户可用参数把程序和数据改到D盘或其他位置；本项目开发机继续使用`D:\WorkBuddyData`。
- ZIP解压位置不是稳定运行位置；完成注册后由安装记录定位正式安装目录。

## 覆盖解压、手动删除和重复注册

覆盖解压是普通用户的主路径，不要求先卸载旧包或清空解压目录：

- 解压目录视为不受控的临时来源。注册前必须逐项校验Manifest中的文件；缺失、篡改或路径越界立即拒绝。
- 正式程序目录从干净staging建立，只复制Manifest白名单文件和Manifest本身。解压目录里的旧版残留、用户误放文件或
  其他额外文件仅记录为`extra_files_ignored`，不复制、不执行。
- 同一版本重复注册视为幂等修复。已有正式程序目录只有在`WORKBUDDY-INSTALL.json`所有权记录有效时才可替换；
  已有同名Skill只有在`WORKBUDDY-RUNTIME.json`所有权记录有效时才可替换。
- 版本相同时执行幂等修复；当前包版本严格更高时执行升级；当前包较旧时拒绝降级。
- 用户手动删除整个正式程序目录、删除一个或两个项目自有Skill后，可从同一或另一解压目录重新运行注册脚本修复。
- 同名外来Skill、损坏或无法识别的所有权记录一律fail closed并原样保留，不猜测所有权。
- 数据目录独立于可重建程序和Skill；修复只补建已知目录，不删除项目、Artifact、配置、模型、缓存和输出。

## 升级、回滚和卸载

- 默认程序目录由Manifest的`package_version`动态生成，不在脚本中硬编码旧版本。
- 升级先验证旧程序和两个Skill的所有权、版本和路径一致性；新旧版本数据根必须继续独立于可重建程序。
- 已注册Skill中的DataRoot必须与本次升级参数一致；不一致时在任何写入前拒绝，避免升级后看起来像用户项目丢失。
- 新程序和Skill进入活动位置后必须运行离线`doctor`。只有`pass/degraded`才提交；失败会删除新版本、恢复旧程序和
  两个旧Skill，用户数据不回滚也不删除。
- 成功升级后只清理所有权已验证的旧程序；旧包降级保持fail closed。
- 普通用户通过`从WorkBuddy卸载.cmd`卸载。程序和匹配所有权的Skill先移出活动位置，再清理；自卸载时由隐藏的
  延迟清理进程等待CMD退出后删除程序目录。
- 卸载默认且固定保留DataRoot；不匹配所有权的同名Skill列为protected并保留。卸载报告写入DataRoot日志目录。

当前合同已经实现跨版本向前升级、失败自动回滚和默认保留数据的卸载，但仍需在最终普通用户Windows环境和真实WorkBuddy中完成验收。

## 尚未通过

- D盘隔离真实环境准备、幂等和本地引擎发现已通过；全新普通Windows默认路径与真实WorkBuddy自然语言全链仍待验收；
- 主动降级、彻底删除DataRoot和未知手工遗留目录清理；
- 真实WorkBuddy普通用户自然语言触发与Human Checkpoint全链验收；
- 真实/付费Provider成片；
- `OFFLINE ADAPTER READY`。
