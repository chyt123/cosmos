import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        pt = math.inf
        ans = 0
        for i in points:
            if i[0] <= pt:
                pt = min(pt, i[1])
            else:
                ans += 1
                pt = i[1]
        return ans + 1
        # points.sort()
        # ans = []
        # for i in points:
        #     if not ans or ans[-1][1] < i[0]:
        #         ans.append(i)
        #     elif ans[-1][0] <= i[0] <= ans[-1][1]:
        #         ans[-1] = [i[0], min(ans[-1][1], i[1])]
        # return len(ans)


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(sol.findMinArrowShots(points))