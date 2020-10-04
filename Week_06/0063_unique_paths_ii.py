from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 新建矩阵版
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        store = [[0] * width for i in range(height)]

        # 从上到下，从左到右
        for m in range(height):  # 每一行
            for n in range(width):  # 每一列
                if not obstacleGrid[m][n]:  # 如果这一格没有障碍物
                    if m == n == 0:  # 或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m - 1][n] if m != 0 else 0  # 上方格子
                        b = store[m][n - 1] if n != 0 else 0  # 左方格子
                        store[m][n] = a + b
        return store[-1][-1]
