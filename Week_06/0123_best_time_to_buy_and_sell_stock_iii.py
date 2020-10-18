from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0

        dp = [[0] * 5 for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(N):
            dp[i][3] = -float("inf")

        for i in range(1, N):
            dp[i][0] = 0
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return max(0, max(dp[N - 1][2], dp[N - 1][4]))

