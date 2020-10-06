from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_mul, min_mul, max_ans = 1, 1, -float("inf")
        for i in range(len(nums)):
            if nums[i] < 0:
                max_mul, min_mul = min_mul, max_mul
            max_mul = max(max_mul * nums[i], nums[i])
            min_mul = min(min_mul * nums[i], nums[i])

            max_ans = max(max_ans, max_mul)
        return max_ans
