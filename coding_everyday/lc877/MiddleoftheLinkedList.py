import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = defaultdict()
        for i in range(n):
            dp[i, i] = - piles[i]

        def find_dp(s, e):
            if (s, e) in dp:
                return dp[s, e]
            if (e - s) % 2 != 0:
                ret = max(piles[s] + find_dp(s + 1, e), piles[e] + find_dp(s, e - 1))
            else:
                ret = min(- piles[s] + find_dp(s + 1, e), - piles[e] + find_dp(s, e - 1))
            dp[s, e] = ret
            return ret
        return find_dp(0, n - 1) > 0


if __name__ == "__main__":
    sol = Solution()
    piles = [5, 3, 4, 5]
    piles = [1, 2, 100, 2, 3, 1]
    piles = [8, 9, 7, 6, 7, 6]
    print(sol.stoneGame(piles))
