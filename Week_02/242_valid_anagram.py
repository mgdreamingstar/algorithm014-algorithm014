import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dicts = collections.defaultdict(int)
        for i in range(len(s)):
            dicts[s[i]] += 1
            dicts[t[i]] -= 1
        for val in dicts.values():
            if val != 0:
                return False
        return True