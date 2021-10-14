import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        stack = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i, j))
        while stack:
            cur_x, cur_y = stack.pop()
            for i in range(m):
                matrix[i][cur_y] = 0
            for i in range(n):
                matrix[cur_x][i] = 0
        for i in matrix:
            print(i)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
    ]
    for i in test_cases:
        print(sol.setZeroes(i))
