import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = 0
        row = 0
        col = 0
        for i in range(len(grid)):
            row_max = 0
            col_max = 0
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    top += 1
                row_max = max(row_max, grid[i][j])
                col_max = max(col_max, grid[j][i])
            row += row_max
            col += col_max

        return top + row + col


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 2], [3, 4]]
    grid = [[2]]
    grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(sol.projectionArea(grid))
