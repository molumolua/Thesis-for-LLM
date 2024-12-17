# 12.15
- 用python程序，其实在读取数学问题，并且转化成变量时就已经存在困难点。
  - 使用prompt 让它尽可能保留，这种问题应该并没有那么普遍。
- 要修改一下代码续写，应该让原本的代码变成加强后的代码的一部分，不规定位置。
  
# 12.16
The value of the expression  \\[(3^{1001}+4^{1002})^2-(3^{1001}-4^{1002})^2\\]is $k\\cdot12^{1001}$ for some positive integer $k$. What is $k$?
```
def solution():
    # Define the variables
    a = 3**1001
    b = 4**1002
    
    # Using the identity (a+b)^2 - (a-b)^2 = 4ab
    expression = (a + b)**2 - (a - b)**2
    simplified_expression = 4 * a * b  # Since a = 3^1001 and b = 4^1002
    
    # Factor out 12^1001 from the expression
    # 12^1001 = (3*4)^1001 = 3^1001 * 4^1001
    # We rewrite 4^1002 as 4^1001 * 4, so the expression becomes:
    # 4 * 3^1001 * 4^1001 * 4
    # = 4^2 * 3^1001 * 4^1001
    # = 16 * 12^1001
    
    # k is the factor in front of 12^1001, which is 16
    k = simplified_expression / (12**1001)
    
    return k
```
从程序的角度来说，他在备注中已经计算出了结果，然后还要用程序去算。
python不能用来证明某个结论，所以某些问题的重心在写备注辅助计算，这些问题有些不太适合我们的加强思路。
# 12.17
- 目前方法加强和程序续写表现不好，程序续写已经修改（未测）
- 阅读 difficult math problem的review
  - 高API调用
  - 高人力
    - 通过训练专门的模型来自动化更多生成和验证步骤，降低对人工审核的依赖
  - 新生成的问题，是out-of-distribution的吗？
    - 和原本的数据集做分布差异分析
    - 和其他OOD数据集上测试模型的性能对比