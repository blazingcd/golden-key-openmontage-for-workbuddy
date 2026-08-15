# WorkBuddy Shell V2 验收矩阵

状态：`FROZEN_BASELINE / STAGE_1_MAY_REFINE_WITHOUT_EXPANDING_SCOPE`

## 1. 状态必须独立报告

| 状态 | 含义 | 不能由什么代替 |
|---|---|---|
| `SHELL_INSTALLED` | Shell和Skill进入受支持安装位置 | ZIP构建成功 |
| `OBJECT_IDENTITY_VERIFIED` | Shell/Core/Release/Manifest/Lock/SHA/安装实例一致 | 文件名、目录名、最新时间 |
| `RUNTIME_BOUND` | 实际CoreRoot、Python、cwd、DataRoot和env被锁定 | Python包存在、doctor文字说明 |
| `REAL_WORKBUDDY` | 真实WorkBuddy客户端在新会话执行 | Codex、CLI、fixture或历史会话 |
| `PROCESS_CORRECT` | Core原生Pipeline/Skill/Artifact/Reviewer/Checkpoint合同正确 | 产生项目目录或MP4 |
| `CAPABILITY_REAL` | 真实工具或能力执行 | mock、静态registry、旧产物 |
| `LOCAL_RENDER_E2E` | 本次运行产生有效本地成片 | 旧成片、单个中间媒体 |
| `BUSINESS_EFFECTIVE` | 用户实际观看并认可业务结果 | ffprobe或自动评分 |
| `REAL_E2E` | 当前定义的完整本地产品链闭环 | 任一局部PASS |
| `STRICT_MANIFEST_CONFORMANCE` | 原生合同严格一致 | 业务效果认可 |
| `PROVIDER_E2E` | 经授权真实调用指定Provider | Key存在、静态配置、费用估算 |
| `PUBLISH_E2E` | 外部发布能力 | 当前项目不适用，记`NOT_APPLICABLE` |

## 2. 通用裁决

- `BLOCKED`：只用于执行前依赖、精确输入或授权未满足；
- `PASS`：精确对象、规定动作、证据和最终退出全部满足；
- `FAIL`：在正确对象和有效执行中证明合同或结果不满足；
- `INCOMPLETE`：执行一旦开始后对象不一致、命令无最终退出、证据缺失、环境干扰或任务被用户停止；
- `NOT_TESTED`：没有执行；
- `NOT_APPLICABLE`：功能不在当前范围；
- `PARTIAL`：只用于明确允许的非二元治理维度，不得替代关键Gate的PASS。

## 3. Gate A：对象与环境

入口：阶段7安装候选通过离线测试并锁定安装对象。

要求：

- literal用户消息不含Core路径、Python或`.venv`；
- 显式Skill正确命中；
- Locator只读取登记对象，不扫盘；
- Launcher绑定精确CoreRoot、Python、cwd和DataRoot；
- 正确环境中的最小Core preflight成功；
- 实际解释器和Core身份进入会话回执；
- Provider调用0、费用0；
- 新增进程和窗口残留为0；临时、测试、重复或旧版本Skill残留为0；正式受支持且身份锁定的目标Skill必须保留，不得误删。

Gate A不证明Pipeline、成片或业务效果。

## 4. Gate B：原生生产入口

入口：Gate A `PASS_ACCEPTED`。

要求：

- WorkBuddy读取已绑定Core自己的Guide；
- OpenMontage Agent自主选择Pipeline；
- Shell没有推荐、覆盖或预填Pipeline；
- 产生Core原生第一阶段Artifact；
- 产生原生Checkpoint或按Manifest进入相应Gate；
- `user_message`与`executor_controls`证据分离。

Gate B不证明最终渲染或业务效果。

## 5. Gate C：本地短成片

入口：Gate B `PASS_ACCEPTED`。

要求：

- 使用无rotation争议的短素材；
- 使用新WorkBuddy会话和新项目；
- Core原生工具真实执行；
- Artifact、Checkpoint、Final Review和结果指针一致；
- Tool正常返回；
- MP4有效；
- Provider调用0、费用0；
- 新增浏览器和进程残留为0；临时、测试、重复或旧版本Skill残留为0；正式受支持且身份锁定的目标Skill必须保留。

Gate C不证明门店竖屏问题已修复。

## 6. Gate D：Core修复后的门店业务验收

入口：

- Gate C `PASS_ACCEPTED`；
- Core项目提供包含方向闭环的新不可变Release、ZIP/SHA/Lock和独立证据；
- Shell通过原子切换登记该新Core。

要求：

- 普通用户消息不包含Core路径、Python、9:16或技术补丁；
- 自动识别素材实际显示方向；
- 不使用Shell transpose、临时预转码Skill或项目级救火脚本；
- 输出正确9:16成片；
- 用户实际观看并确认业务效果；
- `PROCESS_CORRECT`、`LOCAL_RENDER_E2E`和`BUSINESS_EFFECTIVE`分别报告；
- 默认Provider调用=`0`、费用=`0`；
- 若未来确需Provider，必须引用独立、显式的Provider授权和费用授权，并把调用、实际费用、对象和退出状态单独报告；该调用不得使Gate D自动获得`PROVIDER_E2E`，也不得替代Gate E。

## 7. Gate E：可选Provider扩展

Gate E不是Shell V2本地版完成前置，且与Gate D保持独立裁决。

只有用户单独授权后才验证：

- Provider配置和身份；
- 费用披露与预算；
- 网络和真实生成调用；
- Provider返回资产进入Core原生Artifact链；
- 完整成片及费用对账。

Key存在、`present_unverified`、静态registry和Provider菜单均不能证明`PROVIDER_E2E`。

## 8. 真实WorkBuddy测试卡最低身份

首次真实V2验证前必须锁定：

```text
shell_commit
shell_package_version
core_release
core_commit
core_manifest_sha256
core_lock_sha256
install_root
data_root
core_python
skill_hashes
literal_user_message
executor_controls
workbuddy_version
model
global_skill_interference
new_session_id
new_project_id
provider_authorization
cost_authorization
```

任何字段缺失时，真实验收不得开始。
