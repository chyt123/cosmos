class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        dp = [[0] * n for _ in range(n)]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if diff == 2:
                    dp[i][j] = values[i] * values[i+1] * values[j]
                else:
                    dp[i][j] = min(
                        dp[i + 1][j] + values[i] * values[i + 1] * values[j],
                        dp[i][j - 1] + values[i] * values[j - 1] * values[j]
                    )
                    for k in range(i + 2, j - 1):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

        return dp[0][n - 1]

# [0, 0, 3, 7, 10, 15], 
# [0, 0, 0, 12, 7, 22], 
# [0, 0, 0, 0, 4, 9], 
# [0, 0, 0, 0, 0, 20], 
# [0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0]]
