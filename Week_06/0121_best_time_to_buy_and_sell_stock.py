from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        N, minprice = len(prices), prices[0]
        dp = [0] * N
        for i in range(1, N):
            minprice = min(prices[i], minprice)
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]
