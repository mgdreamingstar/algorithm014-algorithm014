class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 100ms
        hash = {}
        for ch in s:
            hash[ch] = hash.get(ch, 0) + 1
        for key in hash.keys():
            if hash[key] == 1:
                return s.index(key)
        return -1


class Solution1:
    def firstUniqChar(self, s: str) -> int:
        # 72ms
        hash = {c: s.count(c) for c in s}
        for c in s:
            if hash[c] == 1:
                return s.index(c)
        return -1
