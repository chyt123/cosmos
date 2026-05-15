class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        fresh_cnt = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        min_passed = 0

        while q and fresh_cnt > 0:
            min_passed += 1

            tmp_list = []
            while q:
                cur_x, cur_y = q.popleft()
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x = cur_x + i
                    new_y = cur_y + j
                    if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_cnt -= 1
                        tmp_list.append((new_x, new_y))
            q.extend(tmp_list)

        return min_passed if fresh_cnt == 0 else -1