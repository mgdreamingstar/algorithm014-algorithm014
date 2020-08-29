import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = collections.Counter(nums)
        hq, ans = [], []
        for key in frequency:
            heapq.heappush(hq, (-frequency[key], key))
        for _ in range(k):
            ans.append(heapq.heappop(hq)[1])
        return ans
