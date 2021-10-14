from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        l = 0
        r = size * size - 1

        def reachable(t: int) -> bool:
            visit = [[False for _ in range(size)] for _ in range(size)]
            queue = [(0, 0)]
            visit[0][0] = True
            while queue:
                x, y = queue.pop(0)
                if x == y == size - 1:
                    return True
                if grid[x][y] <= t:
                    for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        new_x = x + m
                        new_y = y + n
                        if 0 <= new_x < size and 0 <= new_y < size and not visit[new_x][new_y] and grid[new_x][new_y] <= t:
                            queue.append((new_x, new_y))
                            visit[new_x][new_y] = True
            return False

        while l < r:
            m = (l + r) // 2
            if reachable(m):
                r = m
            else:
                l = m + 1

        return l


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    grid = [[3,2],[0,1]]
    print(sol.swimInWater(grid))
