# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把腾讯WorkBuddy可靠连接到经过身份验证、版本化的金钥匙版OpenMontage执行包。WorkBuddy是唯一运行中的Agent；它读取执行包Guide后承担OpenMontage生产角色。Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2：`REOPENED_PACKAGE_REFRESH_REQUIRED`（旧Package为`PASS_ACCEPTED_HISTORICAL`）
- 仓库卫生：`PASS_ACCEPTED`，正式对象`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，精确33文件
- 阶段3规划：`RUNTIME_SCOPE_CORRECTED_FOR_REVIEW`
- 阶段3实现：`NOT_GRANTED`
- 阶段4 Launcher：`NOT_GRANTED`
- 阶段5 WorkBuddy入口：`NOT_GRANTED`
- 阶段6状态结果转交：`NOT_GRANTED`
- 阶段2/3 Runtime纠偏文档：`REVIEW_READY`

当前任务只把阶段2重新登记前置条件、阶段3 Runtime范围及WorkBuddy唯一Agent结论统一到现有权威中，不构成实现授权。实时状态和精确Git对象只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。

当前唯一生产实现是旧Package的Registration与Locator；它是历史已接受证据，不是新版Package验收。重新登记裁决见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力由WorkBuddy依据已验证执行包合同执行，不存在第二个OpenMontage Agent进程。

金钥匙版交付包必须自带经Manifest/Lock固定的私有Python，普通用户不需要系统Python。阶段3只发现并准备闭集运行组件：Python私有依赖、FFmpeg、Node、Remotion、HyperFrames及其锁定浏览器；它只检查受管路径、明确登记的宿主工具或PATH命令解析，不扫描磁盘。缺失项必须先形成missing-only计划、展示下载量/目标/许可并取得用户明确同意。除临时批准且精确锁定的FFmpeg `gyan.dev`资产外，其余下载只允许批准的中国大陆镜像；FFmpeg例外在“不使用代理/VPN的中国大陆网络直连”验证通过前仍不可执行，任何组件都不得自动回退其他海外源。

阶段3至阶段6按编号建设和验收，但用户实际运行从阶段5的显式WorkBuddy入口开始。阶段5先触发阶段2 Locator重验和阶段3单一闭集检查；只有有效Runtime就绪回执才进入阶段4。若缺失，阶段6转交missing-only计划，用户另行授权后由阶段3准备并停止，原生产请求不自动重试。阶段4不启动第二个Agent，只绑定一次WorkBuddy会话；阶段6直接转交Runtime及Launcher事实，除真实格式缺口外不新增转换层。

阶段3任务包已经按条件授权冻结，但当前不是立即实现许可。只有新版阶段2和本轮规划纠偏均独立审阅、进入正式分支，并通过只读交接审计后才能启动。最大实现范围为一个`runtime_prepare.py`公共入口、一个生产Runtime Lock和一个直接测试文件；受管写入只允许位于`<DataRoot>/Runtime`和`<DataRoot>/Caches`。
