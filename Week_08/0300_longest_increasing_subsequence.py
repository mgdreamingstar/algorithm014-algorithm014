from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        for i in range(1, len(nums)):
            left = 0
            right = len(tail)
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tail):
                tail.append(nums[i])
            else:
                tail[left] = nums[i]
        return len(tail)
