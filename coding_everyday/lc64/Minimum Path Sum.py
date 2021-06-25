import collections
import copy
import math
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                up = dp[i - 1][j] if i - 1 >= 0 else math.inf
                left = dp[i][j - 1] if j - 1 >= 0 else math.inf
                dp[i][j] = grid[i][j] + min(up, left)
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = [[1, 2, 3], [4, 5, 6]]
    print(sol.minPathSum(grid))
