import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        dp[1] = 0

        for i in range(3, n + 1):
            for j in range(2, math.floor(math.sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = dp[j] + dp[i // j]
                    break
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.minSteps(n))
