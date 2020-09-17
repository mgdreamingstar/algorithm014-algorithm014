from typing import List


class Solution:
    directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        if board[x][y] == "M":
            # rule 1
            board[x][y] = "X"
        else:
            self.__dfs(board, x, y)
        return board

    def __dfs(self, board, x, y):
        count = 0
        for i in range(8):
            new_x = x + self.directions[i][0]
            new_y = y + self.directions[i][1]
            if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
                continue
            if board[new_x][new_y] == "M":
                count += 1
        if count > 0:
            # rule 3
            board[x][y] = str(count)
        else:
            # rule 2
            board[x][y] = "B"
            for i in range(8):
                new_x = x + self.directions[i][0]
                new_y = y + self.directions[i][1]
                if (
                    new_x < 0
                    or new_x >= len(board)
                    or new_y < 0
                    or new_y >= len(board[0])
                    or board[new_x][new_y] != "E"
                ):
                    continue
                self.__dfs(board, new_x, new_y)


if __name__ == "__main__":
    board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]

    solution = Solution()
    print(solution.updateBoard(board, [3, 0]))