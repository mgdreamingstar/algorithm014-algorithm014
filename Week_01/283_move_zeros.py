from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        i = 1
        while i < len(nums):
            if nums[i] == 0 and nums[j] == 0:
                i += 1
                continue

            if nums[i] != 0 and nums[j] == 0:
                nums[j], nums[i] = nums[i], nums[j]

            i += 1
            j += 1

