import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        s0 = 0
        s1 = -prices[0]
        for i in range(1, l):
            s0 = max(s0, s1 + prices[i] - fee)
            s1 = max(s1, s0 - prices[i])
        return max(s0, s1)


if __name__ == "__main__":
    sol = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(sol.maxProfit(prices, fee))
