from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        d = {x: set() for x in stones}
        d[1].add(1)
        for x in stones[:-1]:
            for j in d[x]:
                for k in range(j - 1, j + 2):
                    if k > 0 and x + k in d:
                        d[x + k].add(k)
        return bool(d[stones[-1]])


if __name__ == '__main__':
    solution = Solution()
    print(solution.canCross([0, 1, 3, 4, 5, 7, 9, 10, 12]))
