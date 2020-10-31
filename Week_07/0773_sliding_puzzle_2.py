from typing import List
from collections import namedtuple
import heapq


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        self.scores 
            意义：数字 0-5 在不同位置的得分
            维度：2 x 3 x 6:
        """
        self.scores = [0] * 6
        goal_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 0: (1, 2)}

        for num in range(6):
            self.scores[num] = [
                [abs(goal_pos[num][0] - i) + abs(goal_pos[num][1] - j) for j in range(3)]
                for i in range(2)
            ]

        Node = namedtuple("Node", ["heuristic_score", "distance", "board"])
        heap = [Node(0, 0, board)]
        visited = []

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if self.get_score(node.board) == 0:
                return node.distance
            elif node.board in visited:
                continue
            else:
                for neighbor in self.get_neighbors(node.board):
                    if neighbor in visited:
                        continue
                    heapq.heappush(
                        heap,
                        Node(
                            node.distance + 1 + self.get_score(neighbor),
                            node.distance + 1,
                            neighbor,
                        ),
                    )
            visited.append(node.board)
        return -1

    def get_neighbors(self, board):
        flat_board = board[0] + board[1]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        now = flat_board.index(0)
        res = []
        for nxt in moves[now]:
            new_board = flat_board[:]
            new_board[nxt], new_board[now] = new_board[now], new_board[nxt]
            res.append([new_board[0:3], new_board[3:6]])
        return res

    def get_score(self, board):
        """
        目前 board 各个数字得分的总和
        """
        return sum([self.scores[board[i][j]][i][j] for i in range(2) for j in range(3)])


if __name__ == "__main__":
    sol = Solution()
    print(sol.slidingPuzzle([[1, 2, 3], [4, 0, 5]]))

