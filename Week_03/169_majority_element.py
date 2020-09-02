import collections


class Solution:
    def majorityElement(nums):
        c = collections.Counter(nums)
        return max(c.keys(), key=c.get)