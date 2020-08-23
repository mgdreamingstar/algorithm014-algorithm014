class Solution1:
    """
    iteration
    """

    def preorder(self, root):
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            n = stack.pop()
            res.append(n.val)
            for child in n.children[::-1]:
                stack.append(child)
        return res


class Solution2:
    """
    recursion
    """

    def preorder(self, root):
        if not root:
            return []

        res = [root.val]

        for child in root.children:
            v = self.preorder(child)
            if v:
                res.extend(v)
        return res

