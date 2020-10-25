from typing import List


class Node:
    pass


def levelOrder(self, root: Node) -> List[List[int]]:
    def traverse_node(node, level):
        """
        这是深度优先，
        当节点没有 children 时，开始回退，然后横向寻找
        """
        if len(result) == level:  # 每次新进入一层，创建
            result.append([])
        result[level].append(node.val)
        for child in node.children:
            traverse_node(child, level + 1)

    result = []

    if root is not None:
        traverse_node(root, 0)
    return result
