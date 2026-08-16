# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把WorkBuddy可靠连接到经过身份验证、版本化的外部OpenMontage执行包。WorkBuddy负责对话，OpenMontage Agent负责生产；Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2：`PASS_ACCEPTED`
- 仓库卫生：`PASS_ACCEPTED`，正式对象`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，精确33文件
- 阶段3规划：`GRANTED`
- 阶段3实现：`NOT_GRANTED`
- 阶段4 Launcher：`NOT_GRANTED`
- 阶段5 WorkBuddy入口：`NOT_GRANTED`
- 阶段6状态结果转交：`NOT_GRANTED`
- 阶段3至阶段6缩减范围：`REVIEW_READY`

当前任务只把阶段3至阶段6的缩减范围统一到现有权威中，不构成实现授权。实时状态和精确Git对象只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。

当前唯一生产实现是Package Registration与Locator。稳定合同见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)，实现证据为`tests/workbuddy/test_package_registration.py`。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力属于已验证外部执行包内的OpenMontage Agent。

阶段3至阶段6没有已验证输入或直接消费者时不得新增生产代码：阶段3允许以无额外Runtime零代码结束，阶段4只启动一个受控Agent进程一次，阶段5只保留一个显式WorkBuddy入口，阶段6优先直接复用Launcher回执。
