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
