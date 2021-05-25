import bisect
import collections
import math
import re
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for idx, i in enumerate(grid):
            if i[0] != 1:
                grid[idx] = [1 - x for x in grid[idx]]

        for i in range(len(grid[0])):
            cur = sum([grid[j][i] for j in range(len(grid))])
            if n - cur > cur:
                for j in grid:
                    j[i] = 1 - j[i]

        suum = 0
        for i in grid:
            num = 0
            for idx, j in enumerate(i[::-1]):
                num += j * 2 ** idx
            suum += num

        return suum


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    print(sol.matrixScore(grid))