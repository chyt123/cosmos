import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        safe_pt = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[safe_pt][1]:
                safe_pt = i
            else:
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    intervals = [[1, 2], [1, 2], [1, 2]]
    print(sol.eraseOverlapIntervals(intervals))