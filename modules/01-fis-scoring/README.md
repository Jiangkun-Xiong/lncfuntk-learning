# 01 / 算懂 FIS：当前起点

当前练习保留在仓库顶层 `scripts/`、`data/`、`vendor/` 和 `outputs/`。本目录是第一阶段的阅读入口。

问题：不同类型的网络邻居如何共同影响 lncRNA 优先级？

- 输入：六个合成候选的 miRNA / TF / PCG 邻居计数。
- 操作：按列缩放，应用固定上游权重，算分、排序并比较替代权重。
- 输出：归一化表、评分表、敏感性表与运行记录。

从仓库根目录运行：

```bash
python scripts/run_demo.py --out outputs/my-first-run --actor learner-local-run
python scripts/test_fis.py
python scripts/check_reference.py --out outputs/my-first-run/reference_check.json
```

## 本人完成门槛

- [ ] 独立运行，找到自己的输出目录。
- [ ] 手算 0.7825，解释 A/B 默认排序。
- [ ] 解释权重或候选集合变化怎样影响结果。
- [ ] 指出未复现的阈值、GO 与生物学验证。
- [ ] 填写[自己的运行记录](../../notes/03_reading_log.md)。

核对基线由助手完成，以上个人任务未自动判定完成。

下一问：[这些邻居数从哪里来？](../02-expression-to-network/README.md)
