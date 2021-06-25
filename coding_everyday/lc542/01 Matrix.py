import collections
import copy
import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[math.inf for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    up = dp[i - 1][j] if i - 1 >= 0 else math.inf
                    left = dp[i][j - 1] if j - 1 >= 0 else math.inf
                    dp[i][j] = min(up, left) + 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if mat[i][j] != 0:
                    down = dp[i + 1][j] if i + 1 < m else math.inf
                    right = dp[i][j + 1] if j + 1 < n else math.inf
                    dp[i][j] = min(dp[i][j], min(down, right) + 1)

        return dp


if __name__ == "__main__":
    sol = Solution()
    mat = [
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0],
    ]
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(sol.updateMatrix(mat))
