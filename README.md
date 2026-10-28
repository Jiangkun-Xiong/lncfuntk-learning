# lncFunTK FIS micro-reproduction / lncFunTK 评分模块学习

An AI-assisted learning scaffold for Jiangkun Xiong, based on the published lncFunTK implementation associated with Hao Sun's research. This is a **small component exercise using synthetic data**, not a paper-level reproduction or a claim of independent bioinformatics proficiency.

[个人主页](https://jiangkun-xiong.github.io/) · [学习路线](https://jiangkun-xiong.github.io/learning/) · [详细学习手册](docs/HANDBOOK.md)

## What this project does

1. Reads six deliberately invented lncRNA neighbor-count profiles.
2. Scales each feature column to [0, 1] with min-max scaling.
3. Reproduces the inspected weighted FIS arithmetic: `0.22 × miRNA + 0.57 × TF + 0.21 × PCG` after scaling.
4. Compares the arithmetic with a minimally adapted upstream `CalFIS.py`, neighbor counts with the original Perl script, and scaling with modern scikit-learn when available.
5. Shows how changing weights changes a ranking. Alternative weights are teaching examples, not fitted or validated models.

## Why this small module

The full lncFunTK integrates RNA-seq, ChIP-seq and CLIP-seq to build regulatory networks and prioritise/annotate lncRNAs. Its original environment requires Python 2.7 and Perl. This exercise isolates an inspectable calculation so that the learner can understand one step before working toward an original demo or real data.

**Upstream:** [zhoujj2013/lncfuntk](https://github.com/zhoujj2013/lncfuntk), commit `65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9`. This author-owned repository is linked to the group's published lncFunTK work; it is not a repository under the `cuhk-haosun` organisation. See [source map](notes/01_source_map.md) and [third-party attribution](THIRD_PARTY.md).

## Quick start

Python 3.9 or later is sufficient for the main demo. From this directory:

```bash
python scripts/run_demo.py --out outputs/my-first-run --actor learner-local-run
python scripts/test_fis.py
python scripts/check_reference.py --out outputs/my-first-run/reference_check.json
```

The reference check always runs the Python 3 arithmetic adapter. The Perl and scikit-learn checks are optional and report `skipped` if those tools are absent. Do not interpret a skipped check as a pass.

To regenerate the invented input data, run `python scripts/make_toy_data.py`.

## Verified initial output

The **assistant**, not the learner, executed the initial scaffold verification on 2026-10-28. The initial run is recorded in `outputs/run_manifest.json` with actor `assistant-initialization`.

| Rank | Synthetic lncRNA | FIS |
| --- | --- | --- |
| 1 | TOY_lnc_A | 0.7825 |
| 2 | TOY_lnc_E | 0.5925 |
| 3 | TOY_lnc_B | 0.5725 |
| 4 | TOY_lnc_C | 0.3375 |
| 5 | TOY_lnc_D | 0.2150 |
| 6 | TOY_lnc_ZERO | 0.0000 |

The arithmetic comparison, Perl neighbor-count comparison and modern scikit-learn scaling comparison all passed in the initial environment. Four hand-calculated/boundary checks also passed. The relevant machine-readable evidence is in [outputs](outputs/).

These numbers describe invented inputs. They are not evidence for real lncRNA function, calibrated probabilities or biological discoveries.

## Current progress and authorship

| Item | Current status | Who completed it |
| --- | --- | --- |
| Public-source inventory and pinned code map | Scaffold prepared | Assistant |
| Synthetic data and small Python 3 demo | Implemented and executed | Assistant |
| Initial component comparisons | Passed in the initial environment | Assistant |
| Learner's own rerun | Pending | Jiangkun to complete |
| Learner's explanation and reading notes | Pending | Jiangkun to complete |
| Full legacy environment / original demo | Not attempted | Future work |
| Real-data / paper-level reproduction | Not attempted | Future work |

## What to do first

- [ ] Run the quick-start commands on your own computer and save your outputs separately.
- [ ] Calculate TOY_lnc_A's score by hand and explain why TOY_lnc_B has more neighbors but a lower default FIS.
- [ ] Open the pinned upstream files in [notes/01_source_map.md](notes/01_source_map.md) and annotate what each one does.
- [ ] Read the lncFunTK paper's workflow figure and record a short explanation in [notes/03_reading_log.md](notes/03_reading_log.md).
- [ ] Explain three things this tiny exercise has not reproduced.

These tasks become learning evidence when you complete and commit your own answers. The scaffold does not pre-fill them as completed.

## What this project excludes

Experimental sequencing processing, network reconstruction from experimental data, weight training, random-network threshold estimation, GO enrichment, and validation of paper findings. In particular, the FIS calculation here is **not** the full functional-lncRNA classification step.

## Files

| Location | Purpose |
| --- | --- |
| `data/` | Six synthetic profiles, a typed toy node list and toy interactions |
| `scripts/` | Demo, arithmetic helpers, reference comparison and boundary checks |
| `vendor/lncfuntk/` | Small attributed upstream source files and one Python 3 compatibility adapter |
| `outputs/` | Initial numerical output, sensitivity analysis and verification evidence |
| `notes/` | Code map, questions, blank personal reading log and interview practice |
| `docs/HANDBOOK.md` | Detailed Chinese learning and interview handbook |
| `ROADMAP.md` | A bounded sequence of learner tasks |

## References

- Zhou et al. (2018), *lncFunTK: a toolkit for functional annotation of long noncoding RNAs*. DOI: [10.1093/bioinformatics/bty339](https://doi.org/10.1093/bioinformatics/bty339).
- Zhou et al. (2017), *LncFunNet: an integrated computational framework for identification of functional long noncoding RNAs in mouse skeletal muscle cells*. DOI: [10.1093/nar/gkx232](https://doi.org/10.1093/nar/gkx232).
- [Hao Sun's CUHK-Shenzhen faculty profile](https://med.cuhk.edu.cn/teacher/1118).

This project is an individual learning exercise and is not affiliated with or endorsed by the original authors or their laboratory.
