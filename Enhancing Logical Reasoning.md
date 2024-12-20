# Abstract
大模型在长推理链的复杂逻辑推理任务中表现不好。
这篇文章使用了合成的图数据进行监督微调，有效提高了特定任务的推理性能，并且在其他任务上保持了相同性能。

# Introduction
大模型在多跳推理任务上表现不好，很难对步骤进行推理，并且易受prompt中的微小扰动影响。

自然语言的推理任务可以表现为有限node和edge的结构化数据，我们可以利用合成的图数据进行特定任务的训练。（归纳和空间推理）

本文贡献：
- 设计了一种基于图的随机游走抽样算法
- 设计了一个prompt策略，能够先提取推理链然后推到出答案（CoT的方式）

# Methodology
facts的结构化表示，可以抽象成图形，例如家庭关系。目标是从这些关系图（异构图）中生成合成示例，以使大模型十影目标推理任务。
## Relational Graph Construction
从初始图只有一个根节点v0开始。在每个迭代l中，
- 从G（l-1）中搜索节点之间不存在的relation
- 如果有发现不存在的关系，则添加具有这些不存在关系的新节点来增长图
- 对于这个新节点，有一个演绎函数来添加这个节点和原本G（l-1）中其他节点的关系

## 子图 sampling
- 不走已经经过的节点，并且根据随机选取先生成一条链c
- 运用增强技术引入多样性和复杂性
  - 置换，指重新排序原本的三元组（vi，r, vi+1）
  - 边噪声，指向顶点vi引入一条在原图但不在链中的边
  - 边方向翻转，指随机反转c中的一些边的方向，该边推理流程
  
## Graph Synthetic Data for LLM Tuning
- 根据目标推理任务构建输入输出对
  - 例如一个 corruption function 从链c中删除一条边，将这条边视作输出y，而剩余的链则用作输入，这种任务可以用于家庭/空间关系的预测。
- 输入c'要转换成自然语言
  - 基于规则的模板
  - 大语言模型
- 一种新的prompt设计，知识模型在生成答案之前先提取关系图

# Experiments
经过上述的SFT，能够在特定任务上强于GPT4o，在其他问题上的能力没有太多变化。