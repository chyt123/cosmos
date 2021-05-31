import copy
import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for diag in range(n // 2):
            l = n - 2 * diag
            tmp = [0] * l
            for i in range(l - 1):
                tmp[i] = matrix[diag][diag + i]
                matrix[diag][diag + i] = matrix[n - diag - i - 1][diag]
                matrix[n - diag - i - 1][diag] = matrix[n - diag - 1][n - diag - i - 1]
                matrix[n - diag - 1][n - diag - i - 1] = matrix[diag + i][n - diag - 1]
                matrix[diag + i][n - diag - 1] = tmp[i]


if __name__ == "__main__":
    sol = Solution()
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2], [3, 4]]
    print(sol.rotate(matrix))
