import math
from typing import List
from collections import defaultdict


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            sqrt_root = math.sqrt(i)
            if int(sqrt_root) == sqrt_root:
                dp[i] = 1
            else:
                miin = math.inf
                for j in range(1, math.floor(math.sqrt(i)) + 1):
                    miin = min(miin, dp[i - j * j])
                dp[i] = 1 + miin
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    for i in range(1, 13):
        print(sol.numSquares(i))
