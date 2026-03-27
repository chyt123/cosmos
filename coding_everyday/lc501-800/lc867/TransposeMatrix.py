import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                ans[i][j] = matrix[j][i]
        return ans


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(sol.transpose(matrix))
