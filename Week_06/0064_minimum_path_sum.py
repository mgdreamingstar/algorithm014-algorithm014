from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [float("INF")] * (len(grid[0]) + 1)
        dp[1] = 0
        for row in grid:
            for ind, num in enumerate(row):
                dp[ind + 1] = min(dp[ind], dp[ind + 1]) + num
        return dp[-1]
