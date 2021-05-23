from typing import List


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] != 1:
                return 0
            cnt = 1
            grid[x][y] = 2  # visited
            cnt += sum(dfs(x + i, y + j) for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)])
            return cnt

        def is_conn(i, j):
            return i == 0 or any(
                [0 <= x < m and 0 <= y < n and grid[x][y] == 2
                 for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]]
            )

        # cal bricks after hits
        for x, y in hits:
            grid[x][y] -= 1

        for i in range(n):
            dfs(0, i)

        # reverse hits and re-cal
        hits.reverse()
        ans = []
        for x, y in hits:
            grid[x][y] += 1
            if grid[x][y] == 1 and is_conn(x, y):
                ans.append(dfs(x, y) - 1)
            else:
                ans.append(0)
        ans.reverse()
        return ans


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 0, 1, 1], [0, 1, 0, 1, 0], [1, 1, 0, 1, 1]]
    hits = [[1, 2], [2, 1], [0, 1], [1, 3]]
    grid = [[1, 0, 0, 0], [1, 1, 1, 0]]
    hits = [[1, 0]]
    grid = [[1, 0, 0, 0], [1, 1, 0, 0]]
    hits = [[1, 1], [1, 0]]
    grid = [[1,1,1],[0,1,0],[0,0,0]]
    hits = [[0,2],[2,0],[0,1],[1,2]]
    grid = [[1], [1], [1], [1], [1]]
    hits = [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]
    print(sol.hitBricks(grid, hits))
