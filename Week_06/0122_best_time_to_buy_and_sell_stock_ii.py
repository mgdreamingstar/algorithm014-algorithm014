from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0

        """
        0: all cash
        1: all stock
        """
        dp = [[0] * 2 for _ in range(N)]
        dp[0][1] = -prices[0]

        for i in range(1, N):
            print(i)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[N - 1][0]

