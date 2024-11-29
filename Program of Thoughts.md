# Abstract
PoT使用语言模型（CodeX）来生成文本和编程语言语句，然后生成答案。

计算委托给了程序解释器，就可以解耦推理和计算（避免语言模型的计算错误）
在数学和金融数据集上比COT提高12%。
# Introduction
CoT在处理数学表达式问题上存在问题：
- 有计算错误
- 无法解决复杂表达式
- 表达遍历时效率很低
# Method
## POT
对于方程式使用SymPy的solve函数解决。
有Few-shot和Zero-shot两种方式，但是Few-shot明显性能大大提高。
# Experiment
GSM8K，SVAMP和MultiArith数据集可以用四舍五入的公差（0.001）来比较答案。

error analysis：
- 值的获取错误 47%
- 逻辑生成错误 33%
