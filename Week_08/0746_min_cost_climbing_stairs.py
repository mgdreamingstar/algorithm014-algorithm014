from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        fn = [cost[0], cost[1]] + [0] * (len(cost) - 1)
        cost = cost + [0]  # 最后位置，添加哨兵节点
        for i in range(2, len(cost)):
            fn[i] = min(fn[i - 1], fn[i - 2]) + cost[i]
        return fn[-1]
