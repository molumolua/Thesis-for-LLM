### 先提取问题中的condition
You are a Mathematics Expert in the field of extracting key information.
Your target is to extract the key mathematical condition and the question  in one given problem.
The result in #Mathematical Conditions#  MUST be the json array in the json format,each item in the array is a string describe the mathematical condition.
You CANNOT omit the non-text parts such as the table and code in #Original Problem#:. Also, please do not omit the input in #Original Problem#.
You SHOULD complicate the #Mathematical Conditions# and #Mathematical Question# using the following method:
Check each token in the problem and identify the definition part and question part of the problem in #Original Problem#.
Identify each condition in the definition part and append it into #Mathematical Conditions#. 
Try you best to find the implied condition in the #Original Problem#. 
Each item in the list in #Mathematical Conditions# MUST contain ONLY ONE mathematical condition.
Fill in the #Mathematical Question# with the question part.
Try your best to make sure we can reconstruct the problem using the extracted #Mathematical Conditions# and #Mathematical Question#.
#Original Problem#:
<Here is instruction.>
#Mathematical Conditions#:
#Mathematical Question#:




#Mathematical Conditions#:

```json
[
    "The Smith family consists of 4 sons.",
    "The Smith family consists of 3 daughters.",
    "There are 7 chairs arranged in a row.",
    "At least 2 boys must be seated next to each other."
]

```
#Mathematical Question#: In how many ways can the Smith family's children be seated in a row of 7 chairs such that at least 2 boys are next to each other?

### 细粒度提取每一步条件，方法，结论
You are a Mathematics Expert in the field of extracting key information in the process.
Your target is to extract the triple of {conditions, method and conclusion} in each step of a given mathematical solution process in #Original Solution#.
The result in #Extract Triples#  MUST be a json array in the json format, and each object in the array describes a single step in the process, including three attributes: conditions, method and conclusion.
You SHOULD make sure the triples are in the order of their appearances in the original solution. 
Strings in #Initial Conditions# indicate the initial condition.
You CANNOT omit the non-text parts such as the table and code in #Original Solution#:. Also, please do not omit the input in #Original Solution#.
You SHOULD complicate the #Extract Triples# using the following method:
Check each step in the process of solution and extract conditions, method and the conclusion.
Conditions in LATER steps MUST be  conclusion in FORMER steps or #Initial Conditions#.
FORMER conclusion are NOT ALLOWED to appear in LATER conclusion.
#Initial Conditions#  are NOT ALLOWED to appear in conclusion.
Conclusion is LIMITED to ONE in each triple and MUST be a phased mathematical objective different from former ones.
You SHOULD  check  the connection between each step and reflect the connection in the exacted triples.
The method in each triple MUST include mathematical knowledge points and calculative process and is ONLY ALLOWED to use information in corresponding conditions in the same triple.
Try your best to make sure we can reconstruct the solution only using the extracted Triples.
#Initial Conditions#:
<Here is Conditions.>
#Original Solution#:
<Here is instruction.>
#Extract Triples#:

```json
[
    {
        "conditions": [
            "The Smith family consists of 4 sons.",
            "The Smith family consists of 3 daughters.",
            "There are 7 chairs arranged in a row.",
            "At least 2 boys must be seated next to each other."
        ],
        "method": "Using complementary counting to focus on counting the arrangements where no two boys are next to each other, which simplifies the problem. Considering one possible arrangement (BGBGBGB) where no two boys are adjacent.",
        "conclusion": "Only one arrangement (BGBGBGB) ensures no two boys are adjacent."
    },
    {
        "conditions": [
            "Only one arrangement (BGBGBGB) ensures no two boys are adjacent."
        ],
        "method": "Calculate the factorial of the number of boys and girls for the specific arrangement BGBGBGB. That is $4!$ for boys and $3!$ for girls.",
        "conclusion": "Total seating arrangements for BGBGBGB is $4! \\times 3! = 144$."
    },
    {
        "conditions": [
            "The Smith family consists of 4 sons.",
            "The Smith family consists of 3 daughters.",
            "There are 7 chairs arranged in a row.",
            "Total seating arrangements for BGBGBGB is $4! \\times 3! = 144$."
        ],
        "method": "Calculate the total number of unrestricted seating arrangements for all 7 children, and subtract the unwanted seating arrangements (where no two boys are next to each other) from it. Total unrestricted arrangements calculated by $7!$.",
        "conclusion": "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896."
    }
]

```

### evolve triples
- 替换步骤
- 增加步骤（可以把一个步骤剖开再加，也可以在answer之后加，也就是修改问题） 
- 测试下来效果不是很满意。

You are a Mathematics Expert.
Your target is to evolve the sequential triples extracted from a mathematical solution into another a bit little more difficult ONE for AI systems to understand and implement, corresponding to more advanced skills in human education system.
The #Original Triples# use the condition in #Original Conditions# to solve a specific question.
You SHOULD complicate the #Evolved Conditions# and #Evolved Triples# using the following method:
ALL the semantics in conditions and conclusion are NOT ALLOWED to edit.
Replace ONLY ONE function in ONE triple in the #Original Triples#  to make the whole list of triples evolve into a bit little more complicated one, but MUST keep the semantic rationality.
You should add ONE or TWO rational conditions if #Original Conditions# DO NOT meet the demand of the new function.
In the replaced triple, you can edit the conditions in the scope of the union of #Evolved Conditions# and conditions in former triples.
In the replaced triple, you MUST calculate the quantitative value of conclusion accurately and simplify it to the simplest form.
In the following triple, you SHOULD check and adapt the quantitative value of conditions and conclusion to fit the replacement. 
Try your best to make sure the generated #Evolved Triples# is rational and logically coherent enough to generate a mathematical solution based on the #Evolved Triples# can actually use the #Evolved Conditions# to solve the  #Original Question#.
You MUST keep #Evolved Conditions# the same format as #Original Conditions# and keep #Evolved Triples# the same format as #Original Triples#.
#Original Conditions#:
<Here is Condition.>
#Original Question#:
<Here is Question.>
#Original Triples#:
<Here is Triples.>
#Evolved Conditions#:

#Evolved Triples#:

### 往后衍生
我们首先先识别（字符串哈希？）我们的conclusion和condition集合，去重。

从已知的一些条件中，运用method构造一个我们可以得到的结论。
- 把条件分成两种，一种是必须包括的（在有向无环图中无后继节点的）
- 另一种是可选的，其他全部条件。
- 要生成的结论不能是重复的，使得我们前序求得的conclusion是没有意义的。如果能够使得必选条件对这个结论来说非常重要，那就可以满足。
  
上述的识别步骤就利用python代码执行，不用大模型操作。
  
我们有了这个方法之后，可以直接在原问题上继续衍生问题，或者说我们截断部分后续的步骤，识别出必选条件。
先不考虑截断，也就是我们目前处理好的条件为：
"Required Conditions":[
   "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896." 
]

"Optional Conditions":[
    "The Smith family consists of 4 sons.",
    "The Smith family consists of 3 daughters.",
    "There are 7 chairs arranged in a row.",
    "At least 2 boys must be seated next to each other.",
    "Only one arrangement (BGBGBGB) ensures no two boys are adjacent.",
    "Total seating arrangements for BGBGBGB is $4! \\times 3! = 144$."
]

You are a Mathematics Expert in construction mathematical process.
Your target is to construct ONE json object in the #Constructed Object# including three attributes: conditions, method and conclusion from given conditions in #Required Conditions# and #Optional Conditions#.
The conditions is a list of strings, method and conclusion is ONE string.
You SHOULD complicate the #Constructed Object# using the following method:
The conditions in the #Constructed Object# MUST contain conditions in #Required Conditions#, and conditions in #Optional Conditions# is Optional.
The method in #Constructed Object# MUST contain mathematical calculation and mathematical knowledge.
The method can be multi-step and SHOULD calculate the target conclusion correctly.
You MUST generate ONE target conclusion in the conclusion #Constructed Object# and we can ONLY use conditions and serval mathematical skill in  method in the #Constructed Object# to generation the target conclusion.
The #Required Conditions# should exerted a decisive effect on the target conclusion, and the target conclusion should have extendibility.
Try your best to make sure the target conclusion aims to solve another definite meaningful mathematical problem and is NOT ALLOWED equal to ANY conditions in #Required Conditions# and #Optional Conditions#. 
Try your best to make sure the generated #Constructed Object# is rational and logically coherent.
You should output FAIL in the #Constructed Object# if you fail to construct the method and conclusion with a definite number.
#Required Conditions#:
<Here is Required Conditions.>
#Optional Conditions#:
<Here is Optional Conditions.>
#Constructed Object#:
```json

{
  "conditions": [
    "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896.",
    "The Smith family consists of 4 sons.",
    "The Smith family consists of 3 daughters.",
    "There are 7 chairs arranged in a row."
  ],
  "method": "Calculate the probability of at least two boys sitting next to each other by dividing the number of desired arrangements (4896) by the total number of possible seating arrangements (7!).",
  "conclusion": "The probability of at least two boys from the Smith family sitting next to each other is 4896 / 5040, approximately 97.14%."
}

```
这个生成虽然没有用到什么更加高级的技巧，但是也算正确的往后走了一步。我们直接把这个加在后面，生成一版新的conditions，再尝试一下往前走一步。
"Required Conditions":[
   "The probability of at least two boys from the Smith family sitting next to each other is 4896 / 5040, approximately 97.14%. 
]
["The proportion of seating arrangements where at least two boys are next to each other is $4896/5040 = 204/210 = 34/35$."]

"Optional Conditions":[
    "The Smith family consists of 4 sons.",
    "The Smith family consists of 3 daughters.",
    "There are 7 chairs arranged in a row.",
    "At least 2 boys must be seated next to each other.",
    "Only one arrangement (BGBGBGB) ensures no two boys are adjacent.",
    "Total seating arrangements for BGBGBGB is $4! \\times 3! = 144$.",
    "Desired seating arrangements with at least two boys next to each other is $7! - (4! \times 3!) = 5040-144 = 4896."
]

- 生成的不太好，我认为问题其实是1.他总会重复步骤，重复之前的method（我们没有给它），2.required conditions没有起到决定性作用。
- 尝试：把之前的步骤也给他，让他不要生成一样的步骤（避免重复），并且以暂时的结论继续往下推（扶正问题的走向，并且告知）


You are a Mathematics Expert in construction mathematical process.
Your target is to construct ONE json object in the #Constructed Object# including three attributes: conditions, method and conclusion from given conditions in #Initial Conditions# and #Process Triples#.
The constructed object is the extension of #Process Triples# and MUST be in the same form of the object in #Process Triples#.
You SHOULD complicate the #Constructed Object# using the following method:
The conditions in the #Constructed Object# MUST contain the conclusion in the LAST triple of the  #Process Triples#, conditions in #Initial Conditions#  and other conclusions are Optional.
The method MUST include mathematical knowledge points and calculative process and is ONLY ALLOWED to use information in corresponding conditions in the same triple.
The method can be multi-step and SHOULD calculate the target conclusion correctly.
The method is NOT ALLOWED make any assumptions or extend the given conditions.
You MUST generate ONE target conclusion in the conclusion of #Constructed Object# and push the whole process into a more complicated one for AI systems.
The LAST triple of the  #Process Triples# should exert a decisive effect on the target conclusion, and the target conclusion should have extendibility.
Try your best to make sure the target conclusion aims to solve another definite meaningful mathematical problem and is NOT ALLOWED equal to ANY other conditions or conclusions. 
Try your best to make sure the generated #Constructed Object# is rational and logically coherent.
#Initial Conditions#:
<Here is Initial Conditions.>
#Process Triples#:
<Here is Process Triples.>
#Constructed Object#:

{
    "conditions": [
        "The Smith family consists of 4 sons.",
        "The Smith family consists of 3 daughters.",
        "There are 7 chairs arranged in a row.",
        "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896."
    ],
    "method": "To further explore the seating possibilities, calculate the probability that any two boys sit next to each other given the desired arrangement count. We use the previously calculated desired arrangement count of 4896. The total possible seating arrangements are $7! = 5040$. Thus, the probability is calculated by dividing the number of desired arrangements by the total arrangements, which gives $\frac{4896}{5040}$.",
    "conclusion": "The probability that any two boys will sit next to each other in the seating arrangement is $\frac{4896}{5040} = \frac{408}{420} = \frac{34}{35}$."
}

{
    "conditions": [
        "The Smith family consists of 4 sons.",
        "The Smith family consists of 3 daughters.",
        "There are 7 chairs arranged in a row.",
        "The probability that any two boys will sit next to each other in the seating arrangement is \(\frac{34}{35}\)."
    ],
    "method": "Extend the analysis by considering the impact of fixing one son in the first chair and arranging the remaining family members. Calculate the number of arrangements where the next chair (second chair) is necessarily occupied by another boy to meet the condition of at least two boys sitting next to each other, using permutations of the remaining members. This can be calculated as \(6!\) arrangements for the remaining members after fixing two boys in the first two chairs.",
    "conclusion": "The number of specific arrangements where at least the first two chairs are occupied by boys is \(6! = 720\). This specific scenario helps understand detailed configurations within the high probability \(\frac{34}{35}\) of boys sitting together."
}

### 允许多做一个假设
You are a Mathematics Expert in construction mathematical process.
Your target is to construct ONE json object in the #Constructed Object# including three attributes: conditions, method and conclusion from given conditions in #Initial Conditions# and #Process Triples#.
The constructed object is the extension of #Process Triples# and MUST be in the same form of the object in #Process Triples#.
You SHOULD complicate the #Constructed Object# using the following method:
The conditions in the #Constructed Object# MUST contain the conclusion in the LAST triple of the  #Process Triples#, conditions in #Initial Conditions#  and other conclusions are Optional.
You can make ONE assumption in the #Constructed Object# and add it into conditions.
Assumption is NOE ALLOWED in the method in the #Constructed Object#.
The method MUST include mathematical knowledge points and calculative process and is ONLY ALLOWED to use information in corresponding conditions in the same triple.
The method can be multi-step and SHOULD calculate the target conclusion correctly.
You MUST generate ONE target mathematic conclusion with a precise number in the primary form in the conclusion of #Constructed Object# and push the whole process into a bit more complicated one for AI systems.
The LAST triple of the  #Process Triples# should exert a decisive effect on the target conclusion, and the target conclusion should have extendibility.
Try your best to make sure the generated #Constructed Object# is rational and logically coherent.
#Initial Conditions#:
<Here is Initial Conditions.>
#Process Triples#:
<Here is Process Triples.>
#Constructed Object#:

{
    "conditions": [
        "The Smith family consists of 4 sons.",
        "The Smith family consists of 3 daughters.",
        "There are 7 chairs arranged in a row.",
        "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896."
    ],
    "method": "To push the complexity further, analyze the probability that a random seating arrangement satisfies the condition of at least two boys next to each other. This is done by dividing the desired seating arrangements by the total unrestricted seating arrangements ($7!$). Calculate this probability and then apply it to a hypothetical scenario where the Smith family attends 3 different events, assuming independent seating arrangements for each event.",
    "conclusion": "The probability of at least two boys sitting next to each other in any given event is $\frac{4896}{5040}$. The probability that this occurs at least once in three events is $1 - (1 - \frac{4896}{5040})^3$, which evaluates to approximately 0.998."
}

{
    "conditions": [
        "The Smith family consists of 4 sons.",
        "The Smith family consists of 3 daughters.",
        "There are 7 chairs arranged in a row.",
        "Desired seating arrangements with at least two boys next to each other is $7! - (4! \\times 3!) = 5040-144 = 4896.",
        "The probability of at least two boys sitting next to each other in any given event is $\frac{4896}{5040}$."
    ],
    "method": "To enhance the complexity, consider the probability that a random seating arrangement does not meet the condition of at least two boys next to each other over multiple events, using binomial probability. Assuming the family attends 5 different events, calculate the probability that the condition is met in at least 4 out of these 5 events. Use the binomial formula $P(X \geq k) = \sum_{i=k}^{n} \binom{n}{i} p^i (1-p)^{n-i}$, where $n=5$, $k=4$, and $p = \frac{4896}{5040}$.",
    "conclusion": "The probability that at least two boys are sitting next to each other in at least 4 out of 5 events is calculated using the binomial formula, resulting in a probability of approximately 0.992."
}


### 向前剖开
把某个initial condition剖开，用一些新的condition，或者其他的initial condition 去生成这个initial condition。