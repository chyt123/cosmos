import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lo = 0
        hi = len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid][0] < newInterval[0]:
                lo = mid + 1
            else:
                hi = mid
        intervals.insert(lo, newInterval)
        ans = intervals[:max(0, lo - 1) + 1]
        for i in range(max(0, lo - 1) + 1, len(intervals)):
            if ans[-1][0] <= intervals[i][0] <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    intervals = []
    newInterval = [5, 7]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    intervals = [[1, 5]]
    newInterval = [2, 7]
    intervals = [[0, 5], [9, 12]]
    newInterval = [7, 16]
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(sol.insert(intervals, newInterval))
