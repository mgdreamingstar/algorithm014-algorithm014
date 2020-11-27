class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = []
        for ch in str:
            if 65 <= ord(ch) <= 90:
                ans.append(chr(ord(ch) + 32))
            else:
                ans.append(ch)
        return "".join(ans)

