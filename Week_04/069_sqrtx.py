class Solution:
    def mySqrt(self, x):
        if x < 0:
            raise Exception("不能输入负数")
        if x == 0:
            return 0
        # 起始的时候在 1, 这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
