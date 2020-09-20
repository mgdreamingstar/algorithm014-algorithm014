class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        pre, curr = 1, 1
        for i in range(1, len(s)):
            tmp = curr
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    curr = pre
                else:
                    return 0
            elif s[i - 1] == "1" or (s[i - 1] == "2" and s[i] >= "1" and s[i] <= "6"):
                curr = curr + pre
            pre = tmp

        return curr


class Solution1:
    def numDecodings(self, s):
        """
            w tells the number of ways
            v tells the previous number of ways
            d is the current digit
            p is the previous digit
        """
        v, w, p = 0, int(s > ""), ""
        for d in s:
            v, w, p = w, (d > "0") * w + (9 < int(p + d) < 27) * v, d
        return w
