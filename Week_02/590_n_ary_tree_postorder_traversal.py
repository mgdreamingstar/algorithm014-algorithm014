def postorder(self, root: "Node") -> List[int]:
    res, stack = [], root and [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        stack += [child for child in node.children if child]
    return res[::-1]