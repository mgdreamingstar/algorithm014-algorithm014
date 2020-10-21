from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(amount + 1):
                if i < coin:
                    continue
                dp[i] += dp[i - coin]
        return dp[amount]
