# 面试练习：先核对自己实际做到了哪一步

## 目前可以准确描述的状态

已建立一个基于 lncFunTK 公开代码的学习框架，助手完成了合成数据上的 FIS 算术验证。本人需要完成独立运行、原文件阅读和结果解释，之后再描述为自己完成的模块学习。

## 完成本人运行和理解后，可以参考的英文表达

> I started with a small, code-level exercise based on lncFunTK. I focused on how the public implementation scales three types of network-neighbour counts and combines them into a Functional Information Score. I used synthetic data and checked the calculation against a minimally adapted upstream script. I have not reproduced the full sequencing-to-network pipeline or the paper's biological results.

练习目标：不用背诵，能够解释每一句的技术含义。只在自己确实完成相应步骤后使用其中的第一人称表述。

## 必须能回答

1. 为什么选择 lncFunTK？它与孙昊团队哪个公开方向相关？
2. 它的完整输入是什么？这个微练习从哪一层开始？
3. miRNA、TF、PCG 三列是什么？与表达量有什么区别？
4. 为什么归一化？按行还是按列？
5. 默认权重从哪里来？这次有没有重新训练？
6. FIS 是概率吗？为什么不能仅由分数范围判断？
7. 权重变化会改变哪些排序？你实际观察到了什么？
8. 原始脚本核对证明了什么？没证明什么？
9. 你还没有复现哪些环节？
10. 下一步如何接入原工具 demo 或真实公开数据？

## 与个人背景连接

可以讲述从临床问题、生理信号处理、模型假设和结果解释中获得的训练。不要把脑血流分析直接等同于组学分析。共同点在于定量问题意识，差异在于测量对象、数据结构、误差来源和验证方式。
