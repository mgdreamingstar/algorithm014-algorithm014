from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board = board[0] + board[1]
        moves = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        q, visited = [(tuple(board), board.index(0), 0)], set()
        while q:
            state, now, step = q.pop(0)
            if state == (1, 2, 3, 4, 5, 0):
                return step
            for next in moves[now]:
                _state = list(state)
                _state[next], _state[now] = _state[now], _state[next]
                _state = tuple(_state)
                if _state not in visited:
                    q.append((_state, next, step + 1))
            visited.add(state)
        return -1
