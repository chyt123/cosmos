import bisect
import collections
import heapq
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []  # heap: [- (yi - xi), xi]
        ans = -math.inf
        for x, y in points:
            while q and x - q[0][1] > k:
                heapq.heappop(q)
            if q:
                ans = max(ans, -q[0][0] + x + y)
            heapq.heappush(q, [x - y, x])
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[[-19,9],[-15,-19],[-5,-8]], 10],
        [[[1, 3], [2, 0], [5, 10], [6, -10]], 1],
        [[[0, 0], [3, 0], [9, 2]], 3],
    ]
    for i, j in test_cases:
        print(sol.findMaxValueOfEquation(i, j))

