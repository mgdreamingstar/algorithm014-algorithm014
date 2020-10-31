from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        启发式搜索：
            利用 曼哈顿距离 衡量 子节点 是否更优，排除非优解，加速遍历。
            heap: [(得分，步数，x，y)]
        """
        n = len(grid)
        if n == 0 or grid[0][0] == 1:
            return -1
        target = (n - 1, n - 1)
        f0 = 2 * n - 2  # score of the source node, it is not important at all
        scores = {(0, 0): f0}
        # heap contains (f,g,row-ind,col-in)
        heap = [(f0, 1, 0, 0)]
        while heap:
            f, g, i, j = heappop(heap)
            if (i, j) == target:
                return g
            if scores[(i, j)] < f:  # Lazy removal
                continue
            children = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
                (i + 1, j + 1),
                (i - 1, j - 1),
                (i + 1, j - 1),
                (i - 1, j + 1),
            ]
            for k, l in children:
                if not (0 <= k < n and 0 <= l < n and grid[k][l] == 0):
                    continue
                heuristic = max(abs(k - target[0]), abs(l - target[1]))
                new_score = heuristic + g + 1
                if new_score < scores.get((k, l), float("inf")):
                    scores[(k, l)] = new_score
                    heappush(heap, (new_score, g + 1, k, l))
        return -1
