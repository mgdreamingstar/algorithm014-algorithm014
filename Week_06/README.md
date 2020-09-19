## 递归
### 代码模板
```python
def recur(level, param):
    // terminator
    if (level > MAX_LEVEL):
        // process result
        return
    
    // process current logic
    process(level, param)

    // drill down
    recur(level + 1, newParam)
    
    // restore current status
```

### 区分动态规划、递归、分治
1. 动态规划、递归和分治 没有**根本上的区别**，关键看有无最优子结构
2. 共性：找到重复子问题
3. 差异性：最优子结构、中途可以淘汰次优解

## 动态规划

1. 打破自己的思维惯性，形成机器思维
2. 基础是理解复杂逻辑的关键
3. 放权也是职业进阶的要点要领

5 步构建动态规划算法：
1. 定义子问题，进行分治
2. 猜递推方程是如何递推的
3. 将子问题的解进行合并
4. 建立递推的状态表，自底向上地递推
5. 解决问题