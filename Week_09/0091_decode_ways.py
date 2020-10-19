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


class Solution3:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        # dp[i]：以 s[i] 结尾的前缀字符串的解码个数

        # 分类讨论：
        # 1、s[i] != '0' 时，dp[i] = dp[i - 1]
        # 2、10 <= s[i - 1..i] <= 26 时，dp[i] += dp[i - 2]
        dp = [0 for _ in range(size)]

        if s[0] == "0":
            return 0
        dp[0] = 1

        for i in range(1, size):
            if s[i] != "0":
                dp[i] = dp[i - 1]

            num = 10 * (ord(s[i - 1]) - ord("0")) + (ord(s[i]) - ord("0"))

            if 10 <= num <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i - 2]
        return dp[size - 1]
