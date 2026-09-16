# 第十一批 B11 最终审计

审计日期：2026-08-31（Asia/Shanghai）

## 执行与去重

- 20 个课题均已建立独立项目，并以题目可识别的 tmux/Codex 窗口名运行。
- 每个实际发送给 Codex CLI 的提示词第一行均精确为用户指定的
  `[$prove-or-disprove-math](C:\Users\87510\\.codex\skills\prove-or-disprove-math\SKILL.md)`。
- 队列峰值并发为 4，未超过用户给定上限；20 个任务均已到达终态，当前活动 Codex CLI 数为 0。
- 与 85 个既往实际研究项目及 B11 内部交叉比对后，20 个题目均未判定为重复。

## 科学终态

- `proved`：2 个。其中 Task 5 是已发表的既有证明，仅完成核验，未冒充新结果，也未生成稿件。
- `open after search`：18 个。均因证明、反例、有限认证或新颖性门槛未通过而停止，没有生成占位 PDF。
- 通过全部数学、文献、引用、构建和版面审计的新稿件：1 个（Task 19）。

## Task 19 发布门槛

- 结论：Albertson 猜想在色数 25 时成立。
- 两条独立精确算术程序均通过；致命或重大证明缺口为 0。
- 五条引用均逐条用官方或一手来源核验；引用键检查为 5/5，缺失 0，未使用 0。
- LaTeX 构建无未定义引用、BibTeX 错误、LaTeX 错误或 overfull/underfull 警告。
- 最终 PDF 共 3 页，逐页视觉复核通过；标题、作者、单位和两封邮箱正确。
- PDF 提取文本未发现 SHA-256、Codex、ChatGPT、OpenAI、prompt、agent 或 workflow 痕迹。
- LaTeX ZIP 已在全新临时目录解压并独立构建成功。
- 稿件尚未经过期刊同行评审或接收；“submission-ready”仅表示内部审计门槛已通过。

完整逐题百分制进度见 `progress.md`；逐题是否生成成果及原因见
`publication_artifacts.md`；去重证据见 `dedup_audit.md`。
