class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        l = len(S)
        dp = [[0 if j != i else 1 for j in range(l)] for i in range(l)]
        for dis in range(1, l):
            for i in range(l - dis):
                j = i + dis
                if S[i] != S[j]:
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
                else:
                    i1 = S.find(S[i], i+1, j)
                    j1 = S.rfind(S[j], i+1, j)
                    if i1 == j1 == -1:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif i1 == j1:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else:
                        repeat = dp[i1+1][j1-1] if i1 < j1 else 0
                        dp[i][j] = dp[i+1][j-1] * 2 - repeat
        return dp[0][l-1] % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    S = 'bccb'
    S = 'aabaa'
    S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
    print(sol.countPalindromicSubsequences(S))
