class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if i > 0:
                    m = matrix[i - 1][j]
                    if j - 1 >= 0:
                        m = min(m, matrix[i - 1][j - 1])
                    if j + 1 < n:
                        m = min(m, matrix[i - 1][j + 1])
                    matrix[i][j] += m

        return min(matrix[-1])