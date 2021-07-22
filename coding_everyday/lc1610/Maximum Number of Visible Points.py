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
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        polar = []
        orig = 0
        for x, y in points:
            dx, dy = x - location[0], y - location[1]
            if dx == dy == 0:
                orig += 1
                continue
            else:
                polar.append(math.atan2(dy, dx) * 180 / math.pi)
        polar += [x + 360 for x in polar]
        polar.sort()
        print(polar)
        l, r = 0, 1
        while r < len(polar):
            if polar[r] - polar[l] > angle:  # expand
                l += 1
            r += 1
        print(l, r)
        return r - l + orig if polar else orig


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[[1,1],[1,1],[1,1]], 1, [1,1]],
        [[[1, 1], [2, 2], [3, 3], [4, 4], [1, 2], [2, 1]], 0, [1, 1]],
        [[[2, 1], [2, 2], [3, 4]], 90, [1, 1]],
        [[[1, 0], [2, 1]], 13, [1, 1]],
    ]
    for i, j, k in test_cases:
        print(sol.visiblePoints(i, j, k))

