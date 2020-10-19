class Solution:
    def numSquares(self, n: int) -> int:
        def is_dividable(n, count):
            if count == 1:
                return n in squares
            for sq in squares:
                if is_dividable(n - sq, count - 1):
                    return True
            return False

        squares = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        for count in range(1, n + 1):
            if is_dividable(n, count):
                return count
