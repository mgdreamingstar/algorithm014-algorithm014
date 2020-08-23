## 树的面试题解法一般都是递归，为什么？
对于树形结构的数据，一般遍历方法比较复杂。而使用递归进行遍历，则比较简洁有效。

树的遍历 demo：
```python
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)

```

## 二叉堆
二叉堆需满足的条件：
1. 必须是完全二叉树
2. 父节点大于两个子节点

二叉堆虽然实现简单，但效率一般。它的节点在数组中的索引如下：
1. 父亲节点为 `i`
2. 左子节点为 `2*i + 1`
3. 右子节点为 `2*i + 2`
4. 由子节点查找父节点为 `floor((j - 1)/ 2)`

二叉树插入操作的顺序：
1. 插入到叶子节点
2. 依次和父节点比较，然后交换