from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        l = len(grid)

        def check(x, y) -> bool:
            return 0 <= x < l and 0 <= y < l and grid[x][y] != -1

        dp = [[[-1 for _ in range(l)] for _ in range(l)] for _ in range(l)]
        dp[0][0][0] = grid[0][0]
        for x1 in range(0, l):
            for y1 in range(0, l):
                for x2 in range(0, l):
                    y2 = x1 + y1 - x2
                    if check(x1, y1) and check(x2, y2):
                        cherry = grid[x1][y1]
                        cherry += 0 if x1 == x2 and y1 == y2 else grid[x2][y2]
                        dp1 = dp[x1-1][y1][x2-1] if check(x1-1, y1) and check(x2-1, y2) else -1
                        dp2 = dp[x1-1][y1][x2] if check(x1-1, y1) and check(x2, y2-1) else -1
                        dp3 = dp[x1][y1-1][x2-1] if check(x1, y1-1) and check(x2-1, y2) else -1
                        dp4 = dp[x1][y1-1][x2] if check(x1, y1-1) and check(x2, y2-1) else -1
                        if sum([dp1, dp2, dp3, dp4]) != -4:  # the point is reachable
                            dp[x1][y1][x2] = cherry + max(dp1, dp2, dp3, dp4)
        return dp[l-1][l-1][l-1] if dp[l-1][l-1][l-1] != -1 else 0


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
    print(sol.cherryPickup(grid))
    grid = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
