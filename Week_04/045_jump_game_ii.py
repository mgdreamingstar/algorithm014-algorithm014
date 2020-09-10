from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans, end, max_pos = 0, 0, 0
        for i in range(len(nums) - 1):
            max_pos = max(nums[i] + i, max_pos)
            if i == end:
                end = max_pos
                ans += 1
        return ans