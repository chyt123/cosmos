import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        found = False
        while i < m:
            if matrix[i][0] <= target <= matrix[i][n - 1]:
                found = True
                break
            i += 1
        if not found:
            return False
        arr = matrix[i]
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                r = mid
            else:
                l = mid + 1
        return arr[r] == target


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 5],
        [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
    ]
    for i, j in test_cases:
        print(sol.searchMatrix(i, j))
