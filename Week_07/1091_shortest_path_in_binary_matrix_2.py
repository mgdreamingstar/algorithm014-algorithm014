from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:  # 若起始点或终点堵塞，则不可能有这样的路径
            return -1
        if n == 1:
            return 1
        res = 1  # 注意题目的描述，是返回从 1 到 k 的路径，第一个节点被定为下标 1
        path = deque()
        path.append([0, 0])  # 先压入起点
        while path:  # BFS模板
            for _ in range(len(path)):  # 对BFS的某一层的中所有点向8个方向进行扩展
                x, y = path.popleft()
                for new_x, new_y in [
                    [x - 1, y - 1],
                    [x - 1, y],
                    [x - 1, y + 1],
                    [x, y - 1],
                    [x, y + 1],
                    [x + 1, y - 1],
                    [x + 1, y],
                    [x + 1, y + 1],
                ]:
                    # 下面几种continue可以合并一行，这里为看的清楚就分开写了
                    if new_x == n - 1 and new_y == n - 1:  # 如果扩展的点到达了终点
                        return res + 1
                    if not 0 <= new_x < n or not 0 <= new_y < n:  # 扩展的点超出边界，则跳过
                        continue
                    if grid[new_x][new_y] == 1:  # 若扩展的点为阻塞，则跳过
                        continue
                    if grid[new_x][new_y] == -1:  # 若扩展的点已经访问过，则跳过
                        continue
                    if grid[new_x][new_y] == 0:  # 若为通畅点
                        grid[new_x][new_y] = -1  # 当前层次下已经访问该点
                        path.append([new_x, new_y])  # 将扩展的点加入path，到下一层的时候继续扩展
            res += 1  # 对某一层的元素都求判定过后，距离加1(同一个层次中的所有点的距离距离起点都是相等的）
        return -1
