class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        head = 0
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x, y = 0, 0
        for i in instructions:
            if i == "L":
                head -= 1
            elif i == "R":
                head += 1
            else:
                dx, dy = dir[head % 4]
                x += dx
                y += dy
        
        if head % 4 != 0 or x == y == 0:
            return True
        return False

