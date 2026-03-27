import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return l1 + l2 - 2 * dp[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    word1 = 'abcde'
    word2 = 'cafce'
    word1 = "sea"
    word2 = "eat"
    word1 = "leetcode"
    word2 = "etco"
    print(sol.minDistance(word1, word2))
