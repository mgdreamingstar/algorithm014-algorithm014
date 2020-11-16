from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        for li in intervals:
            if not merged or merged[-1][1] < li[0]:
                merged.append(li)
            else:
                merged[-1][1] = max(merged[-1][1], li[1])
        return merged
