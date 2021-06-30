import bisect
from typing import List
from collections import defaultdict


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for _ in range(l1)] for _ in range(l2)]

        if text2[0] == text1[0]:
            dp[0][0] = 1
        for i in range(1, l1):
            if text2[0] == text1[i] or dp[0][i - 1]:
                dp[0][i] = 1
        for i in range(1, l2):
            print(text2[i])
            if text1[0] == text2[i] or dp[i - 1][0]:
                dp[i][0] = 1

        for i in range(1, l2):
            for j in range(1, l1):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # for i in dp:
        #     print(i)
        return dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    text1 = "abcde"
    text2 = "afgce"
    text1 = "bsbininm"
    text2 = "jmjkbkjkv"
    print(sol.longestCommonSubsequence(text1, text2))
