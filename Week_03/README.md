## 递归
类似循环，利用函数体来进行的循环。递归和循环没有明显的边界。

递归的代码模板：
```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
       
    # process logic in current level
    process(level, data ...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # recursion the current level status if needed
```

### 思维要点

1. 不要人肉进行递归（不要依赖手写递归树）
2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3. 数学归纳法思维

### 其他要点
二叉搜索树的**中序遍历**是递增的。

## 分治和回溯
### 分治
一个复杂问题，应该是由多个部分组成，如果可以找到重复性，即可分解成多个子问题来解决，即为分治。

1. 寻找重复性
2. 分解成子问题
3. 组合每个子问题的结果

```python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
       
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblem
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
```

### 回溯
回溯法采用试错的思想，它尝试分步去解决一个问题。在分步解决问题的时，如果有的答案不对，可以取消上一步或几步的计算，重新尝试其他可能的分步。

回溯法常常用最简单的递归方法来实现，可能出现的情况：
1. 找到一个可能存在的正确的答案
2. 尝试所有可能的分步方法后，宣布没有答案

最坏情况下，分治算法的时间复杂度会达到指数时间 O(2^n)。

#### 回溯的详解

[这篇文章](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw/) 详细讲了回溯的整体思路。

回溯算法和深度优先搜索有异曲同工之妙，它们都是尽可能深地搜索，当遇到问题再向上回溯，重新寻找可能的路径。

回溯算法解决全排列问题的过程：
1. 每一个结点表示了求解全排列问题的不同的阶段，这些阶段通过变量的「不同的值」体现，这些变量的不同的值，称之为「状态」；
2. 使用深度优先遍历有「回头」的过程，在「回头」以后， 状态变量需要设置成为和先前一样 ，因此在回到上一层结点的过程中，需要撤销上一次的选择，这个操作称之为「状态重置」；
3. 深度优先遍历，借助系统栈空间，保存所需要的状态变量，在编码中只需要注意遍历到相应的结点的时候，状态变量的值是正确的，具体的做法是：往下走一层的时候，path 变量在尾部追加，而往回走的时候，需要撤销上一次的选择，也是在尾部操作，因此 path 变量是一个栈；
4. 深度优先遍历通过「回溯」操作，实现了全局使用一份状态变量的效果。

回溯算法需要设计**状态变量**，它们用于指示目前回溯的**层数**、**问题是否解决**、**元素是否已用**等状态。并且，需要注意的是，如果需要向上回溯，那么状态变量需要同步修改。

另外，如果使用列表传递状态，注意在必要的地方将值拷贝（深拷贝、浅拷贝），否则最后状态改变，因结果还指向此地址，所以会返回错误结果。

由于回溯算法的时间复杂度很高，因此在遍历的时候，如果能够提前知道这一条分支不能搜索到满意的结果，就可以提前结束，这一步操作称为**剪枝**。剪枝是一种技巧，通常需要根据不同问题场景采用不同的剪枝策略，需要在做题的过程中不断总结。
