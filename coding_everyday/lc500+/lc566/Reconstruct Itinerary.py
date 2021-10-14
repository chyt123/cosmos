import bisect
import collections
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        row = 0
        col = 0
        for i in range(m):
            for j in range(n):
                new_mat[row][col] = mat[i][j]
                if col == c - 1:
                    row += 1
                    col = 0
                else:
                    col += 1
        return new_mat


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[[1, 2], [3, 4]], 1, 4],
        [[[1, 2], [3, 4]], 2, 4],
    ]
    for i, j, k in test_cases:
        print(sol.matrixReshape(i, j, k))
