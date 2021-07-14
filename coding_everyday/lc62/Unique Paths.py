import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    continue
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 7],
        [3, 2],
        [7, 3],
        [3, 3],
    ]
    for i, j in test_cases:
        print(sol.uniquePaths(i, j))
