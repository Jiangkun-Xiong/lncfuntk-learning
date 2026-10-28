# 从原始代码找到这一小步

核对日期：2026-10-28。上游固定提交：`65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9`。

| 上游文件 | 需要看懂什么 | 本练习覆盖范围 |
| --- | --- | --- |
| [README.md](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/README.md) | 项目目的、输入、Python 2.7 / Perl 环境 | 公开资料梳理 |
| [FunctionalityPrediction.pl](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/FunctionalityPrediction/FunctionalityPrediction.pl) | 抽取 miRNA/TF/PCG 邻居数，归一化、算分，再估计随机网络阈值 | 只覆盖归一化与算分 |
| [ScaleMaxMin.py](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/Training/ScaleMaxMin.py) | 调用 MinMaxScaler，按特征列缩放 | 与现代 sklearn 做数值核对 |
| [CalFIS.py](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/FunctionalityPrediction/CalFIS.py) | 对三列归一化值做加权求和 | 与保留原算式的 Python 3 适配版核对 |
| [pretrained.weight.value.lst](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/Training/pretrained.weight.value.lst) | 默认权重 miRNA 0.22 / TF 0.57 / PCG 0.21 | 使用同一默认权重 |
| [StatNetworkDegree.pl](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/FunctionalityPrediction/StatNetworkDegree.pl) | 从有类型的图节点统计邻居 | 在合成图上运行原始 Perl 文件并核对计数 |
| [CalFdr4FIS.pl](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/FunctionalityPrediction/CalFdr4FIS.pl) | 原流程如何由随机网络分数取阈值 | 未运行；不能宣称完成 FDR 筛选 |
| [GoEnrichment.py](https://github.com/zhoujj2013/lncfuntk/blob/65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9/bin/FunctionalAnnotation/GoEnrichment.py) | GO 功能注释的另一步 | 未复现 |

## 三个容易混淆的点

1. RNA-seq 表达矩阵不是 FIS 的直接输入。本练习从网络已经变成邻居数之后开始。
2. 原工具使用机器学习获得权重，但检查到的 `CalFIS.py` 这一步直接输出加权和，没有调用 sigmoid。因此本练习不把 0 到 1 的分数解释为“有功能的概率”。
3. 评分、设阈值、GO 注释是不同步骤。只算出 FIS，不等于已经筛出了具有生物学功能的 lncRNA。

## 待本人补写

- 我实际打开了哪些文件：
- 我能解释的一段代码及行号：
- 我暂时看不懂的两个地方：
- 我对默认权重迁移到其他细胞系统的疑问：
