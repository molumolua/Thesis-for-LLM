# Introduction
使用program作为验证器来在自集成之前检验。
Plan and Solve Prompt
# Method
先promptLLM生成计划和解决方案，再prompt将生成的计划和解决方案转化为python程序，如果程序和方案匹配，则有效，否则无效。该过程是zero-shot的。

