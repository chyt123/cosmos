from collections import deque


class Solution(object):
    def containVirus(self, grid):
        rst = 0
        while 1:
            visited = [[False for _ in xrange(len(grid[0]))] for _ in xrange(len(grid))]
            regions = list()
            perimeters = list()
            dq = deque()
            return_flag = True
            for i in xrange(len(grid)):
                for j in xrange(len(grid[0])):
                    if grid[i][j] == 1 and not visited[i][j]:
                        return_flag = False
                        # bfs
                        dq.append((i, j))
                        visited[i][j] = True
                        tmp = list()
                        p = 0
                        while dq:
                            (x, y) = dq.popleft()
                            if x + 1 < len(grid) and grid[x + 1][y] == 1 and not visited[x + 1][y]:
                                dq.append((x + 1, y))
                                visited[x + 1][y] = True
                            if x - 1 >= 0 and grid[x - 1][y] == 1 and not visited[x - 1][y]:
                                dq.append((x - 1, y))
                                visited[x - 1][y] = True
                            if y + 1 < len(grid[0]) and grid[x][y + 1] == 1 and not visited[x][y + 1]:
                                dq.append((x, y + 1))
                                visited[x][y + 1] = True
                            if y - 1 >= 0 and grid[x][y - 1] == 1and not visited[x][y - 1]:
                                dq.append((x, y - 1))
                                visited[x][y - 1] = True
                            tmp.append((x, y))
                            if x + 1 < len(grid) and not grid[x + 1][y]:
                                p += 1
                            if x - 1 >= 0 and not grid[x - 1][y]:
                                p += 1
                            if y + 1 < len(grid[0]) and not grid[x][y + 1]:
                                p += 1
                            if y - 1 >= 0 and not grid[x][y - 1]:
                                p += 1

                        regions.append(tmp)
                        perimeters.append(p)
            if return_flag:
                return rst
            curr_idx = perimeters.index(max(perimeters))
            rst += perimeters.pop(curr_idx)
            clean = regions.pop(curr_idx)
            for (x, y) in clean:
                grid[x][y] = 2
            # expand
            for idx, region in enumerate(regions):
                for (x, y) in region:
                    if x + 1 < len(grid) and not grid[x + 1][y]:
                        grid[x + 1][y] = 1
                    if x - 1 >= 0 and not grid[x - 1][y]:
                        grid[x - 1][y] = 1
                    if y + 1 < len(grid[0]) and not grid[x][y + 1]:
                        grid[x][y + 1] = 1
                    if y - 1 >= 0 and not grid[x][y - 1]:
                        grid[x][y - 1] = 1

            for row in grid:
                print row
            print


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 0, 0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 1, 0]]
    grid = [[0,1,0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0,0,0],[0,0,1,1,1,0,0,0,1,0],[0,0,0,1,1,0,0,1,1,0],[0,1,0,0,1,0,1,1,0,1],[0,0,0,1,0,1,0,1,1,1],[0,1,0,0,1,0,0,1,1,0],[0,1,0,1,0,0,0,1,1,0],[0,1,1,0,0,1,1,0,0,1],[1,0,1,1,0,1,0,1,0,1]]
    for row in grid:
        print row
    print
    print sol.containVirus(grid)
