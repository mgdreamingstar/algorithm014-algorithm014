class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans, even = "", True
        for i in range(0, len(s), k):
            ans += s[i : i + k][::-1] if even else s[i : i + k]
            even = not even
        return ans
