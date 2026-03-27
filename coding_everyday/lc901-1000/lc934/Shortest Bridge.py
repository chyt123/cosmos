import collections
import math
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = [-1, 0, 1, 0, -1]
        q = collections.deque()
        level = 0

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2
            q.append([x, y])
            for i in range(4):
                newx = x + d[i]
                newy = y + d[i + 1]
                dfs(newx, newy)

        fin = False
        for i in range(m):
            if fin:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    fin = True
                    break

        while q:
            l = len(q)
            for _ in range(l):
                curx, cury = q.popleft()
                for i in range(4):
                    newx = curx + d[i]
                    newy = cury + d[i + 1]
                    if newx < 0 or newy < 0 or newx >= m or newy >= n or grid[newx][newy] == 2:
                        continue
                    if grid[newx][newy] == 1:
                        return level
                    if grid[newx][newy] == 0:
                        q.append([newx, newy])
                        grid[newx][newy] = 2
            level += 1


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
    grid = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    grid = [[0, 1], [1, 0]]
    print(sol.shortestBridge(grid))


