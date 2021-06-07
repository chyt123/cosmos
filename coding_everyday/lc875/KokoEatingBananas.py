import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import TreeNode, lc_list2tree


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            return sum(math.ceil(i / k) for i in piles) <= h

        lo = 1
        hi = max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    sol = Solution()
    piles = [3, 6, 7, 11]
    h = 8
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(sol.minEatingSpeed(piles, h))
