import collections
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.sum_matrix = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                self.sum_matrix[i][j] = self.sum_matrix[i - 1][j] + \
                                        self.sum_matrix[i][j - 1] + \
                                        self.matrix[i - 1][j - 1] - \
                                        self.sum_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_matrix[row2 + 1][col2 + 1] - \
               self.sum_matrix[row2 + 1][col1] - \
               self.sum_matrix[row1][col2 + 1] + \
               self.sum_matrix[row1][col1]


if __name__ == "__main__":
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    region = [
        [2, 1, 4, 3],
        [1, 1, 2, 2],
        [1, 2, 2, 4]
    ]
    num_matrix = NumMatrix(matrix)
    for x, y, z, w in region:
        print(num_matrix.sumRegion(x, y, z, w))
