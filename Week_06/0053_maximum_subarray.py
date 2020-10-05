from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] + [0] * len(nums)
        max_subsum = nums[0]
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_subsum = max(max_subsum, dp[i])
        return max_subsum
