class Solution:
    def largestValues(self, root):
        if not root:
            return []

        res = []
        queue = [[root]]
        while queue:
            this_level = queue.pop(0)
            next_level = []
            temp = []
            for node in this_level:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(max(temp))
            if next_level != []:
                queue.append(next_level)
        return res
