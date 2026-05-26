class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(x, y):
            if grid[x][y] == 1:
                grid[x][y] = 2
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        dfs(x + dx, y + dy)

        for i in range(m):
            dfs(0, i)
            dfs(n - 1, i)
        for j in range(n):
            dfs(j, 0)
            dfs(j, m - 1)

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt += 1

        return cnt
        
