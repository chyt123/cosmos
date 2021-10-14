import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        miin = math.inf
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < miin:
                miin = prices[i]
            max_profit = max(max_profit, prices[i] - miin)
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 6, 4, 3, 1]
    prices = [7, 1, 5, 3, 6, 4]
    prices = [2, 4, 1]
    print(sol.maxProfit(prices))
