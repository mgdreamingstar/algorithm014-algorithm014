from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        block = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != ".":
                    if val in row[i] | col[j] | block[i // 3 * 3 + j // 3]:
                        return False
                    else:
                        row[i].add(val)
                        col[j].add(val)
                        block[i // 3 * 3 + j // 3].add(val)
        return True
