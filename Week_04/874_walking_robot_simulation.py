class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        x = 0
        y = 0
        best = 0
        dx = 0
        dy = 1
        obstructionSet = set(map(tuple, obstacles))
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for i in range(command):
                    if (x + dx, y + dy) in obstructionSet:
                        break
                    else:
                        x += dx
                        y += dy
                best = max(best, x * x + y * y)
        return best
