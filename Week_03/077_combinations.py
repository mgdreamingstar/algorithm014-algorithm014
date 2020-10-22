from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 特判
        if n <= 0 or k <= 0 or k > n:
            return []
        res = []
        self.__dfs(1, k, n, [], res)
        return res

    def __dfs(self, start, k, n, path, res):
        if len(path) == k:
            res.append(path[:])
            return

        # 注意：这里 i 的上限是归纳得到的
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            self.__dfs(i + 1, k, n, path, res)
            path.pop()