import collections
import math
from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def land_locked_area(self, maps):
        m = len(maps)
        n = len(maps[0])

        def dfs_colored_water(x, y):
            d = [
                [-1, -1],
                [-1, 0],
                [-1, 1],
                [0, 1],
                [1, -1],
                [1, 0],
                [1, 1],
                [0, -1]
            ]
            if x < 0 or y < 0 or x >= m or y >= n or maps[x][y] is not False:
                return
            maps[x][y] = 2
            for i, j in d:
                dfs_colored_water(x + i, y + j)

        for i in range(n):
            if not maps[0][i]:
                dfs_colored_water(0, i)
            if not maps[m - 1][i]:
                dfs_colored_water(m - 1, i)
        for i in range(m):
            if not maps[i][0]:
                dfs_colored_water(i, 0)
            if not maps[i][n - 1]:
                dfs_colored_water(i, n - 1)

        def dfs_cal_area(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or maps[x][y] == 2:
                return 0
            maps[x][y] = 2
            ans = 1
            d = [-1, 0, 1, 0, -1]
            for i in range(4):
                ans += dfs_cal_area(x + d[i], y + d[i + 1])
            return ans

        ret = 0
        for i in range(m):
            for j in range(n):
                if maps[i][j] != 2:
                    ret = max(ret, dfs_cal_area(i, j))

        return ret


if __name__ == "__main__":
    sol = Solution()
    maps = [
        [False, True, True, True, False],
        [False, True, False, True, False],
        [False, True, True, True, False],
        [False, False, False, False, False],
    ]
    maps = [
        [False, False, False, False, False],
        [False, True, True, False, False],
        [False, False, False, True, False],
        [False, False, False, False, True],
    ]
    print(sol.land_locked_area(maps))
