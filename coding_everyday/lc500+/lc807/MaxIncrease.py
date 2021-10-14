from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        order = len(grid)
        trans_grid = [[grid[j][i] for j in range(order) ] for i in range(order)]
        skyline_h = [max(i) for i in grid]
        skyline_v = [max(i) for i in trans_grid]
        increase = 0
        for i in range(order):
            for j in range(order):
                increase += min(skyline_h[i], skyline_v[j]) - grid[i][j]
        return increase


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(sol.maxIncreaseKeepingSkyline(grid))
