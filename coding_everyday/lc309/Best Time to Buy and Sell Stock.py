import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        State machine:

     -- s0 <------ s2
     |->  \       /
           \ buy / sell
            \   /
             s1
             |-|
        """
        n = len(prices)
        s0 = [0 for _ in range(n)]
        s1 = [0 for _ in range(n)]
        s2 = [0 for _ in range(n)]
        s1[0] = -prices[0]
        for i in range(1, n):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[-1], s2[-1])


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 6, 2, 4, 6, 1, 7]
    print(sol.maxProfit(prices))
