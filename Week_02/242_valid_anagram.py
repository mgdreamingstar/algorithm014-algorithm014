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
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        
        if s_counter - t_counter != collections.Counter():
            return False
        return True