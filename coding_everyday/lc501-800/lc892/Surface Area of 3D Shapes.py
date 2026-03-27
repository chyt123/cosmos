import collections
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                self_surface = 2 + grid[i][j] * 4 if grid[i][j] != 0 else 0
                overlap = 0
                if 0 <= i - 1 < m:
                    overlap += min(grid[i][j], grid[i - 1][j])
                if 0 <= j - 1 < n:
                    overlap += min(grid[i][j], grid[i][j - 1])
                ans += self_surface - overlap * 2
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[2]],
        [[1, 2], [3, 4]],
        [[1, 0], [0, 2]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
    ]
    for i in test_cases:
        print(sol.surfaceArea(i))


