from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        v = 0
        i = 0
        j = len(height) - 1
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            if v < area:
                v = area
        return v
