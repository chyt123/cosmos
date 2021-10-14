import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1 or obstacleGrid[i - 1][j - 1] == 1:
                    continue
                dp[i][j] += dp[i - 1][j] if obstacleGrid[i - 2][j - 1] != 1 else 0
                dp[i][j] += dp[i][j - 1] if obstacleGrid[i - 1][j - 2] != 1 else 0
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        [[0, 1], [0, 0]],
    ]
    for i in test_cases:
        print(sol.uniquePathsWithObstacles(i))
