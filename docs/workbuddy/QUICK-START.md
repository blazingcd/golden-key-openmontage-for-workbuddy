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

普通Windows用户不需要预先安装Python。ZIP带有只供本项目使用的便携Python 3.13.15和pip引导wheel；它不会注册成
系统Python，也不会修改PATH。Node、FFmpeg、Remotion、HyperFrames和浏览器仍在用户确认后准备到DataRoot。

安装结束和 WorkBuddy 首次调用都会运行只读 `doctor`，检查 Core 合同、4条业务Pipeline和完整视频制作环境。
检查不会调用真实或付费 Provider，也不会自动下载缺失组件。MCP默认不启用，CLI仍是权威回退。

如果完整环境未就绪，WorkBuddy会把它解释为“准备完整视频制作环境”，先说明下载、磁盘位置以及FFmpeg和Remotion
许可提示，再询问一次。只有用户明确同意后，它才会调用`runtime prepare --confirm-download`，把Python依赖、
FFmpeg、Node、Remotion、HyperFrames和托管浏览器统一准备到所选`<DataRoot>/Runtime`。它不会修改系统Python、
系统PATH或要求管理员权限。默认数据目录在`%LOCALAPPDATA%`；若安装时把`DataRoot`改到D盘，运行时与缓存也在D盘。
当前锁定计划给出的预估下载量为约0.5–1.2GB，安装后占用约1.2–3GB；这是规划区间，npm镜像、Python依赖版本和
压缩率会让实际数值变化，WorkBuddy应以`runtime plan`返回的当前区间为准。

普通用户不需要先理解Remotion或HyperFrames，也不在安装阶段二选一；两条本地合成能力都会准备好。真正制作视频时，
WorkBuddy再根据方案用普通语言解释可用路径、给出推荐，并按Core提案规则等待批准。用户若暂不准备环境，仍可继续
新手引导、方案讨论和API Key配置，但本地媒体处理与最终合成会保持阻断。

ZIP本身仍然是轻量调用包：只携带便携Python引导，不直接携带上述大型视频运行时。Python引导资产由
`WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json`固定并校验；后续下载内容由`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`固定并校验。
当前Windows FFmpeg包为GPLv3构建；Remotion是否免费取决于其官方团队规模和自动化使用条件，较大团队或特定自动化
场景可能需要商业许可。

## 配置图像、视频和配音API密钥

真正调用文生图、图生视频、文生视频、TTS或数字人等在线能力前，还需要配置相应Provider的API Key。
不要把Key粘贴进WorkBuddy聊天或普通命令参数。

1. 在WorkBuddy中说明本次需要“生成图片、生成视频、中文配音、数字人”中的哪些能力；它会显示一到两个推荐
   Provider、厂商直连或第三方网关、官方Key入口、账户权限和费用提醒。
2. 用户明确同意现在配置后，由WorkBuddy打开可见的本地向导；如果无法自动打开，再双击已安装目录中的
   `配置API密钥.cmd`。
3. 在本地窗口先选择目标能力，再选择推荐Provider；Key通过隐藏输入框录入，不在聊天中发送。
4. Key使用Windows当前用户DPAPI加密，保存到`<DataRoot>/Config/golden-key-provider-credentials.json`；
   不写入ZIP解压目录、项目Artifact、WorkBuddy聊天或安装日志。
5. 回到WorkBuddy后让它重新检查配置。`已录入但未验证`只表示Key存在，不代表账号权限、余额或网络连通性已通过。

新手引导应根据当前视频目标只推荐需要的能力，不要求一次配齐所有Provider。配置Key本身不会触发联网、付费生成或
Provider连通性测试；这些动作仍需单独说明并获得用户明确同意。

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
- 如果当前ZIP比已注册版本新，安装器会执行升级：先保留旧程序和Skill，安装并检查新版本，成功后才清理旧程序；
  检查失败会恢复旧版本。旧ZIP低于已注册版本时拒绝降级。
- 升级时继续使用原DataRoot；如果高级参数误指向另一个数据目录，安装器会在写入前拒绝，不会把WorkBuddy切到空目录。

## 卸载

1. 双击当前已安装目录或对应解压包中的`从WorkBuddy卸载.cmd`。
2. 卸载器核验`WORKBUDDY-INSTALL.json`和两个Skill的`WORKBUDDY-RUNTIME.json`，只删除确认属于本项目的内容。
3. 用户数据默认保留；最后一次报告写入`<DataRoot>/Logs/WORKBUDDY-LAST-UNINSTALL.json`。

默认保留内容包括`Projects`、Artifact、配置、模型、缓存、运行时和输出。若同名Skill的所有权记录被修改或不匹配，
该Skill会列为`protected_skills`并原样保留。当前不提供“顺便彻底删除所有用户数据”的按钮，避免普通卸载误删成果。

升级失败自动回滚已实现；主动运行旧ZIP降级仍被禁止，也没有盲目扫描磁盘删除用户手工遗留的未知目录。

## 高级用户手动检查

通常由WorkBuddy完成以下对话和调用。需要手动排查时，可通过已安装的`golden-key-workbuddy.ps1`运行：

```powershell
.\golden-key-workbuddy.ps1 runtime plan --json
.\golden-key-workbuddy.ps1 runtime prepare --confirm-download --json
.\golden-key-workbuddy.ps1 doctor --json
```

第二条命令会访问Python包源、Node/FFmpeg发行源、npm和浏览器发行源，因此必须在用户确认下载、存储和许可提示后
运行；它不会调用视频、图像、语音或其他付费Provider。
