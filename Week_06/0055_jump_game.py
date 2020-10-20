from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i, jump in enumerate(nums):
            if end >= i and i + jump > end:
                end = i + jump
        return end >= i
