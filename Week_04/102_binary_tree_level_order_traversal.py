from typing import List


class TreeNode:
    pass


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans, queue = [[root.val]], [[root]]
        while queue:
            now = queue.pop(0)
            level = []
            for node in now:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level != []:
                ans.append([node.val for node in level])
                queue.append(level)
        return ans

