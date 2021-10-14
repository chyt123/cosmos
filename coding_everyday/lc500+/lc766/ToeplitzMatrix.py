from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for idx, r in enumerate(matrix):
            cur = [r[i] for i in range(0, len(r))]
            if idx == 0:
                pre = cur
                continue
            if not cur[1:] == pre[:-1]:
                return False
            pre = cur
        return True


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    matrix = [[1, 2], [2, 2]]
    print(sol.isToeplitzMatrix(matrix))
