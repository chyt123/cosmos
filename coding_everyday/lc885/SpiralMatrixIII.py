import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        idx = 0
        flag = True
        cnt = 1
        ans = [[rStart, cStart]]
        last = [rStart, cStart]
        while len(ans) < rows * cols:
            for i in range(cnt):
                new_row = last[0] + d[idx % 4][0]
                new_col = last[1] + d[idx % 4][1]
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    ans.append([new_row, new_col])
                last = [new_row, new_col]
            if flag:
                flag = False
            else:
                flag = True
                cnt += 1
            idx += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    rows = 5
    cols = 6
    rStart = 1
    cStart = 4
    rows = 1
    cols = 4
    rStart = 0
    cStart = 0
    print(sol.spiralMatrixIII(rows, cols, rStart, cStart))
