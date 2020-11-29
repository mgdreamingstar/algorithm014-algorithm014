from typing import List


class Solution:
    # 32ms
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        N = len(min(strs, key=len))
        ans = [""]
        for i in range(N):
            ch = strs[0][i]
            for s in strs[1:]:
                if s[i] == ch:
                    continue
                else:
                    return "".join(ans)
            ans.append(ch)
        return "".join(ans)


class Solution1:
    # 40ms
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        start, end, res = strs[0], strs[-1], ""
        for i in range(len(start)):
            if start[i] and start[i] == end[i]:
                res += start[i]
            else:
                break
        return res

