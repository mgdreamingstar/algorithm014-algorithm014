from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for num in arr2:
            while num in arr1:
                ans.append(arr1.pop(arr1.index(num)))
        ans.extend(sorted(arr1))
        return ans
