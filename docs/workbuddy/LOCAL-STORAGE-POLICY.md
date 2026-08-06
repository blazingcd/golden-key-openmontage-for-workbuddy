# WorkBuddy本地存储策略

状态：`W1 ACTIVE`

日期：2026-08-06

## 默认根目录

Windows开发和最终安装默认使用：

```text
D:\WorkBuddyData\
├── Projects\   # 用户项目、Artifact与最终输出
├── Caches\     # Release、pip和可再生成下载缓存
├── Models\     # 本地模型和权重
├── Temp\       # pytest、构建和解压临时目录
├── Logs\       # 脱敏后的本地日志
├── Jobs\       # W2/W3长任务持久状态
└── Dev\venvs\ # 开发期Python隔离环境
```

运行以下命令建立用户数据目录并检查当前机器：

```powershell
golden-key-workbuddy doctor --data-root D:\WorkBuddyData --create-dirs
```

## 开发环境规则

- Python虚拟环境放在`D:\WorkBuddyData\Dev\venvs\`。
- pip缓存放在`D:\WorkBuddyData\Caches\pip\`。
- 测试前将`TEMP`、`TMP`、`PYTHONPYCACHEPREFIX`和pytest `--basetemp`指向`D:\WorkBuddyData\Temp\`。
- Release缓存放在`D:\WorkBuddyData\Caches\golden-key-workbuddy-core\<tag>\`。
- 已由系统安装管理的Python Launcher、Node或FFmpeg可以保留在C盘；本项目不得复制第二份到C盘。

## 数据与安全

- `.env`和Provider凭据不得进入Git、报告、测试夹具或普通日志。
- `Projects`、`Models`、`Temp`、`Logs`和`Jobs`不属于Core同步范围。
- 缓存和临时文件可重建；用户项目和最终输出不得被升级或卸载流程默认删除。
- `Jobs`保存消费方任务JSON、每任务短期锁和数据根级单执行槽；任务记录不复制输入正文，只保存项目内输入路径、
  SHA-256、状态和本地执行结果。跨项目并发固定为1，运行时截止时间只报警、不强杀阻塞Tool。成功终态可幂等读取，
  中断任务必须显式恢复为失败并释放遗留执行槽，不自动重试。
- W1只建立目录和检查能力；W2任务入口仍不调用真实/付费Provider。

W4安装器仍需验证全新Windows用户、升级、卸载和数据保留语义；本策略本身不代表安装验收通过。
