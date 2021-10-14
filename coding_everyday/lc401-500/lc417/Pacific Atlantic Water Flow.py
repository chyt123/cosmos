import bisect
import collections
import math
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        is_pacific = [[False for _ in heights[0]] for _ in heights]
        is_atlantic = [[False for _ in heights[0]] for _ in heights]

        def dfs(x, y, visited, pre):
            if visited[x][y] or heights[x][y] < pre:
                return
            visited[x][y] = True
            d = [-1, 0, 1, 0, -1]
            for i in range(4):
                newx = x + d[i]
                newy = y + d[i + 1]
                if 0 <= newx < m and 0 <= newy < n:
                    dfs(newx, newy, visited, heights[x][y])

        for i in range(m):
            dfs(i, 0, is_pacific, 0)
            dfs(i, n - 1, is_atlantic, 0)

        for j in range(n):
            dfs(0, j, is_pacific, 0)
            dfs(m - 1, j, is_atlantic, 0)

        ans = []
        for i in range(m):
            for j in range(n):
                if is_pacific[i][j] and is_atlantic[i][j]:
                    ans.append([i, j])
        return ans


if __name__ == "__main__":
    sol = Solution()
    heights = [[2, 1], [1, 2]]
    heights = [[1, 1], [1, 1], [1, 1]]
    heights = [[10,10,10],[10,1,10],[10,10,10]]
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(sol.pacificAtlantic(heights))


