class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        connected = set()
        def dfs (x, y, val):
            connected.add((x, y))
            dir = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in dir:
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == val and (x + dx, y + dy) not in connected:
                    dfs(x + dx, y + dy, val)

        dfs(row, col, grid[row][col])

        border = set()
        for (i, j) in connected:
            dir = [(1,0), (-1,0), (0,1), (0,-1)]
            for dx, dy in dir:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx == n or ny < 0 or ny == m or \
                        grid[nx][ny] != grid[row][col]:
                    border.add((i, j))

        # print(connected, border)
        for (i, j) in border:
            grid[i][j] = color
        return grid

# 1 1 1 2 2
# 2 1 2 2 2
# 1 1 2 2 1