import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s0 = 0
        s1 = -prices[0]
        for i in range(1, len(prices)):
            s0 = max(s0, s1 + prices[i])
            s1 = max(s1, s0 - prices[i])
        return max(s0, s1)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [7, 6, 4, 3, 1],
        [7, 1, 5, 3, 6, 4],
        [2, 4, 1]
    ]
    for i in test_cases:
        print(sol.maxProfit(i))
