from typing import List
from collections import defaultdict


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in matrix[0]] for _ in matrix]
        maax = 0
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            maax = max(maax, dp[0][i])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maax = max(maax, dp[i][0])

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if matrix[i][j] == '1' else 0
                maax = max(maax, dp[i][j])
        return maax ** 2


if __name__ == "__main__":
    sol = Solution()
    matrix = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "1"]
    ]
    matrix = [["0", "1"], ["1", "0"]]
    print(sol.maximalSquare(matrix))
