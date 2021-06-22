import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maax = 0

        def dfs(x, y):
            if grid[x][y] in [0, 2]:
                return 0
            cnt = 1
            dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            grid[x][y] = 2
            for i, j in dire:
                cnt += dfs(x + i, y + j) if 0 <= x + i < m and 0 <= y + j < n else 0
            return cnt

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    maax = max(maax, dfs(i, j))
        return maax


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(sol.maxAreaOfIsland(grid))
