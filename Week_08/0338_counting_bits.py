from typing import List


class Solution1:
    # 76 ms
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i & (i - 1)] + 1
        return ans


class Solution2:
    # 96 ms
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(1, num + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


class Solution3:
    # 76 ms
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        for i in range(num + 1):
            if i % 2 == 1:
                ans[i] = ans[i // 2] + 1
            else:
                ans[i] = ans[i >> 1]
        return ans
