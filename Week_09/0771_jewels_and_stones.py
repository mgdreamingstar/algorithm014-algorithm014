class Solution:
    # 40ms
    def numJewelsInStones(self, J: str, S: str) -> int:
        temp, ans = 0, 0
        for ch in J:
            temp |= 1 << (ord(ch) - ord("A"))
        for ch in S:
            if temp & 1 << (ord(ch) - ord("A")):
                ans += 1
        return ans


class Solution1:
    # 36ms
    def numJewelsInStones(self, J: str, S: str) -> int:
        from collections import Counter

        j = set(J)
        return sum(v for k, v in Counter.items() if k in j)
