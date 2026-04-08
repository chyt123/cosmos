class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = [[0 for i in range(n*3)] for j in range(n*3)]
        nm = len(m)
        for i in range(n):
            for j, gj in enumerate(grid[i]):
                if gj == '/':
                    m[i*3][j*3 + 2] = 1
                    m[i*3 + 1][j*3 + 1] = 1
                    m[i*3 + 2][j*3] = 1
                elif gj == '\\':
                    m[i*3][j*3] = 1
                    m[i*3 + 1][j*3 + 1] = 1
                    m[i*3 + 2][j*3 + 2] = 1

        cnt = 0
        for i in range(nm):
            for j in range(nm):
                if m[i][j] == 0:
                    cnt += 1
                    m[i][j] = 2
                    s = [(i,j)]
                    while len(s):
                        x, y = s.pop()
                        for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx, ny = x + a, y + b
                            if 0 <= nx < nm and 0 <= ny < nm and m[nx][ny] == 0:
                                m[nx][ny] = 2
                                s.append((nx, ny))
        return cnt
