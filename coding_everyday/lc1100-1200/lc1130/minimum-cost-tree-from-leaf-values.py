class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        m = [[0] * n for _ in range(n)]
        dp = [[float('inf')] * n for _ in range(n)]
        for diff in range(0, n):
            for i in range(n - diff):
                j = i + diff
                if diff == 0:
                    dp[i][i] = 0
                    m[i][j] = arr[i]
                else:
                    m[i][j] = max(m[i][j - 1], arr[j])
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + m[i][k] * m[k + 1][j])

        # for i in dp:
        #     print(i)
        return dp[0][n - 1]
