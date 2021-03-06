import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        j 是右指针
        i 是左指针
        """

        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        needCnt, i, res = len(t), 0, (0, float("inf"))
        for j, c in enumerate(s):
            if need[c] > 0:  # 开始移动右指针
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    c = s[i]
                    if need[c] == 0:
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 记录结果
                    res = (i, j)
                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return "" if res[1] > len(s) else s[res[0] : res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果

