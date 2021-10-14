import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[-1] if dp[-1] != math.inf else -1


if __name__ == "__main__":
    sol = Solution()
    coins = [2]
    amount = 3
    coins = [2147483647]
    amount = 2
    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))
