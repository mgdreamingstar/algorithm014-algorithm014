from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        1st Solution (slow):
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            for j in range(i + 1, len(nums)):
                if nums[j] == b:
                    return [i, j]
                    
        2nd Solution (fast):
        """
        hash_nums = dict(zip(nums, range(len(nums))))
        for ind, num in enumerate(nums):
            if target - num in hash_nums and ind != hash_nums[target - num]:
                return [ind, hash_nums[target - num]] 