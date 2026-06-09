class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        n = len(grid)
        q = set()
        q.add((0,0))
        cnt = 1
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        while q:
            tmp = set()
            for xi, yi in q:
                if (xi, yi) == (n - 1, n - 1):
                    return cnt
                grid[xi][yi] = 2
                for dx, dy in dir:
                    nx = xi + dx
                    ny = yi + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        tmp.add((nx, ny))

            q = tmp
            cnt += 1
        return -1


# 100
# 110
# 110
