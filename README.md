# lncFunTK learning / 从评分到功能假设

**贯穿问题：如何依据数据选择值得验证的 lncRNA，并说明选择的理由与边界？**

An individual learning project starting from a small FIS-scoring exercise, then tracing its inputs, functional interpretation and biological context. This is not the original lncFunTK software or a paper-level reproduction.

[个人主页](https://jiangkun-xiong.github.io/) · [学习主线](LEARNING_MAP.md) · [学习手册](docs/HANDBOOK.md) · [迁移来源](MIGRATION.md)

## One path, four linked questions

| 阶段 | 为什么学 | 可检查产出 | 状态 |
| --- | --- | --- | --- |
| [01 算懂 FIS](modules/01-fis-scoring/README.md) | 候选如何得到分数？ | 自己运行、手算并解释 A/B 排序 | 合成基线已核对；本人任务待完成 |
| [02 追溯输入](modules/02-expression-to-network/README.md) | 邻居数从哪里来？ | 样本表、矩阵说明、小型边表及规则解释 | 下一阶段规划 |
| [03 功能解释](modules/03-function-and-validation/README.md) | 分数能支持什么假设？ | 背景集合说明与功能假设卡 | 依赖前一阶段 |
| [04 领域背景](modules/04-stem-cell-context/README.md) | 干细胞问题中什么算合适证据？ | 两条自己的文献证据记录 | 摘要可并行读；解释待完成 |

先掌握一个可运行的小模块，再向前追溯输入、向后检查解释。完整工具的数据处理顺序仍是实验数据、网络、评分与功能解释。单细胞是[问题需要时再进入的分支](extensions/single-cell/README.md)。

## Current runnable exercise

Python 3.9+ is sufficient for the main demo. Run from this repository's root:

```bash
python scripts/run_demo.py --out outputs/my-first-run --actor learner-local-run
python scripts/test_fis.py
python scripts/check_reference.py --out outputs/my-first-run/reference_check.json
```

Six invented lncRNA profiles are scaled by feature column to [0, 1], then combined using the inspected upstream default weights:

```text
FIS = 0.22 × scaled_miRNA + 0.57 × scaled_TF + 0.21 × scaled_PCG
```

| Rank | Synthetic candidate | Default FIS |
| --- | --- | --- |
| 1 | TOY_lnc_A | 0.7825 |
| 2 | TOY_lnc_E | 0.5925 |
| 3 | TOY_lnc_B | 0.5725 |
| 4 | TOY_lnc_C | 0.3375 |
| 5 | TOY_lnc_D | 0.2150 |
| 6 | TOY_lnc_ZERO | 0.0000 |

The initial scaffold and baseline were prepared and executed with AI assistance on 2026-10-28. Arithmetic, original Perl neighbor counting and modern scikit-learn scaling comparisons passed, along with four hand-calculated/boundary checks. See [verification evidence](outputs/reference_check.json) and [run manifest](outputs/run_manifest.json). Missing optional tools report `skipped` in a learner's reference check.

Synthetic scores are not biological findings or calibrated probabilities. Experimental-data preprocessing, network integration, weight training, random-network thresholding, GO enrichment and paper validation have not been reproduced here.

## Make the next record your own

- [ ] Independently run the demo and locate your output files.
- [ ] Hand-calculate A's 0.7825 and explain why B's higher total neighbor count does not give it a higher default FIS.
- [ ] Explain one ranking change in the sensitivity output.
- [ ] Inspect the [source map](notes/01_source_map.md).
- [ ] Complete one entry in [your reading and run log](notes/03_reading_log.md).

Pending learner tasks remain pending. Later areas have questions, prerequisites and outputs, rather than an unconnected software list.

## Where work belongs

| Location | Purpose |
| --- | --- |
| `data/`, `scripts/`, `vendor/`, `outputs/` | Runnable FIS micro-exercise and preserved baseline |
| `modules/` | Four stages, task briefs and evidence templates |
| `extensions/` | Conditional learning branches |
| `notes/` | Source map, exercises and personal reading/run log |
| `docs/HANDBOOK.md` | Reference handbook; current priorities follow LEARNING_MAP.md |
| `MIGRATION.md`, `migration_source.json` | Original location, commit and snapshot evidence |

## Attribution

Upstream: [zhoujj2013/lncfuntk](https://github.com/zhoujj2013/lncfuntk), pinned at `65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9`. Original notices and file hashes are retained; see [THIRD_PARTY.md](THIRD_PARTY.md).

- Zhou et al. (2018), lncFunTK. DOI: [10.1093/bioinformatics/bty339](https://doi.org/10.1093/bioinformatics/bty339).
- Zhou et al. (2017), LncFunNet. DOI: [10.1093/nar/gkx232](https://doi.org/10.1093/nar/gkx232).

This learning project is not affiliated with or endorsed by the original authors or their laboratory.
