import bisect
import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
        return False

        # for i in matrix:
        #     if target > i[-1]:
        #         continue
        #     idx = bisect.bisect_left(i, target)
        #     if i[idx] == target:
        #         return True
        # return False
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    print(sol.searchMatrix(matrix, target))
