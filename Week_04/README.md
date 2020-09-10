## DFS 和 BFS
### 深度优先搜索
代码模板

#### 递归写法
```python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 

	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
```

#### 非递归写法
```python
def DFS(self, tree): 

	if tree.root is None: 
		return [] 

	visited, stack = [], [tree.root]

	while stack: 
		node = stack.pop() 
		visited.add(node)

		process (node) 
		nodes = generate_related_nodes(node) 
		stack.push(nodes) 

	# other processing work 
	...
```

### 广度优先搜索
代码模板

```python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
    ...
```

## 二分查找
### 二分查找的前提
1. 目标函数的单调性（单调递增或递减）
2. 存在上下界（bounded）
3. 能够通过索引访问（index accessible）

### 代码模板

```python
left, right = 0, len(array) - 1
while left <= right:
    # mid = (left + right) / 2
    mid = (right - left) / 2 + left
    if array[mid] == target:
        # find the target !!
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

## 贪心算法和动态规划
### 动态规划
动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分（即子问题），再根据子问题的解以得出原问题的解。

通常许多子问题非常相似，为此动态规划法试图仅仅解决每个子问题一次，从而减少计算量：一旦某个给定子问题的解已经算出，则将其记忆化存储，以便下次需要同一个子问题解之时直接查表。这种做法在重复子问题的数目关于输入的规模呈指数增长时特别有用。

**重叠子问题**、**最优子结构**、**状态转移方程**就是动态规划三要素。

思考状态转移方程可以如下：
明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。

1. 状态：原问题和子问题中会变化的变量
2. base case：状态最初时的情况
3. 选择：导致状态改变的行为
4. dp 函数/数组：计算/存储状态改变过程

```python
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
```

[labuladong 的动态规划文章](https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-wei-lai-bu-ke/) 总结的很好。

### 贪心算法
贪心算法的**难点**在于，如何判断使用贪心的条件和方式。有时需要将问题转化，有时需要在执行过程中做判断。

贪心算法、回溯和动态规划的对比：
1. 贪心算法：当下做局部最优判断
2. 回溯：能够回退
3. 动态规划：最优判断+回退