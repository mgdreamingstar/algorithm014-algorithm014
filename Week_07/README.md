## Trie 树

Trie 是一颗非典型的多叉树模型，即每个结点的分支数量可能为多个。但是它和一般的多叉树不一样，尤其在结点的数据结构设计上。其结点中并没有直接保存字符值的数据成员，而是保存了对当前结点而言下一个可能出现的所有字符的链接，因此我们可以通过一个父结点来预知它所有子结点的值。

### Tire 树的性质

1. Trie 的形状和单词的插入或删除顺序无关，也就是说对于任意给定的一组单词，Trie 的形状都是唯一的。
2. 查找或插入一个长度为 L 的单词，访问 next 数组的次数最多为 L+1，和 Trie 中包含多少个单词无关。
3. Trie 的每个结点中都保留着一个字母表，这是很耗费空间的。如果 Trie 的高度为 n，字母表的大小为 m，最坏的情况是 Trie 中还不存在前缀相同的单词，那空间复杂度就为 O(m^n)。

最后，关于 Trie 的应用场景：一次建树，多次查询。

### Trie 的实现

```python
class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"
    
    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node
    
    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```
### 212 单词搜索时间复杂度分析

1. 首先需要遍历二维网格中的所有单元，假设网格有 m 行，n列，则时间复杂度为 O(mn)
2. 第一步有 4 个方向选择，之后每一步不能回退，所以有 3 个方向选择
3. 假设单词最大长度为 L，则回溯搜索过程中最多遍历 4 * 3^(L-1) 个单元格
4. 故，总的时间复杂度为 O(4mn*3^(L-1))


## 并查集

### 代码模板

```python
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i):   # 函数名有时为：find
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩
		x = i; i = p[i]; p[x] = root 
	return root
```