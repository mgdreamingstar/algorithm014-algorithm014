import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        hq, ans = [], []
        for key in frequency:
            heapq.heappush(hq, (-frequency[key], key))  # 取负，因为默认为小顶堆
        for _ in range(k):
            ans.append(heapq.heappop(hq)[1])
        return ans
