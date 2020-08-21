from typing import List


def largestRectangleArea(self, heights: List[int]) -> int:
    res = 0
    heights = [0] + heights + [0]
    stack = [0]

    for i in range(1, len(heights)):
        while heights[i] < heights[stack[-1]]:
            cur_height = heights[stack.pop()]
            cur_width = i - stack[-1] - 1
            res = max(res, cur_height * cur_width)
        stack.append(i)
    return res
