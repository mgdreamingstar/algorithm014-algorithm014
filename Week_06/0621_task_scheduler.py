from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        count_max = count.most_common(1)[0][1]  # 相同类出现的最大次数
        tasks_max = Counter(count.values()).get(count_max)  # 相同类出现次数最多的类数量
        res = (count_max - 1) * (n + 1) + tasks_max
        return max(len(tasks), res)
