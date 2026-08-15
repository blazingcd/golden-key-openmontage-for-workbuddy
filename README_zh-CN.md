# 金钥匙 WorkBuddy Shell V2

WorkBuddy Shell V2负责把WorkBuddy可靠连接到经过身份验证、版本化的外部OpenMontage执行包。WorkBuddy负责对话，OpenMontage Agent负责生产；Shell只负责六个模块：安装与生命周期、执行包登记与定位、Runtime按需准备、会话Launcher、WorkBuddy入口、状态与结果转交。

当前状态：

- 阶段1：`PASS_ACCEPTED`
- 阶段2：`PASS_ACCEPTED`
- 阶段3规划：`GRANTED`
- 阶段3实现：`NOT_GRANTED`

本次仓库清理不构成阶段3实现。实时状态和精确Git对象只以[`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md)为准。

当前唯一生产实现是Package Registration与Locator。稳定合同见[`docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`](docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md)，实现证据为`tests/workbuddy/test_package_registration.py`。

本仓库不得运行或指挥视频Pipeline、Provider或媒体生产；这些能力属于已验证外部执行包内的OpenMontage Agent。
