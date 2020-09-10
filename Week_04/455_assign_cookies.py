from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if g is None or s is None:
            return 0
        gi, si = 0, 0
        s.sort()
        g.sort()
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
            si += 1
        return gi
