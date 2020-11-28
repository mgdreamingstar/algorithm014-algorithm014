class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0:
            if s[end] == " ":
                end -= 1
            else:
                break
        start = end
        while start >= 0:
            if s[start] != " ":
                start -= 1
            else:
                break
        return end - start
