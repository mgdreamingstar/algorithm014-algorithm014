from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("INF")] * amount
        for i in range(amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != float("INF") else -1