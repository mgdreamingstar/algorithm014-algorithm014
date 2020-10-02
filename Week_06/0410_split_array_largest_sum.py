from typing import List


class Solution:
    def splits(self, nums, max_sum_sub):
        split = 1
        cur_sub_sum = 0
        for num in nums:
            if cur_sub_sum + num > max_sum_sub:
                cur_sub_sum = 0
                split += 1
            cur_sub_sum += num

        return split

    def splitArray(self, nums: List[int], m: int) -> int:
        maxium, sums = max(nums), sum(nums)
        left, right = maxium, sums

        while left < right:
            mid = left + (right - left) // 2
            split_it = self.splits(nums, mid)
            if split_it > m:
                left = mid + 1
            else:
                right = mid

        return left
