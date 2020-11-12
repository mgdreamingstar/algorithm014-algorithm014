class Solution(object):
    def solveNQueens(self, n):
        def valid(row, col, track):
            if col in track:  # 判列
                return False
            for k in range(row):  # 判斜对角
                if row + col == k + track[k] or row - col == k - track[k]:
                    return False
            return True

        def backtrack(row, track):
            if row == n:  # 已到最后一行
                res.append(track)
                return
            for col in range(n):
                if valid(row, col, track):  # 若位置合法，则进入下一行
                    backtrack(row + 1, track + [col])

        res = []
        backtrack(0, [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in l] for l in res]

