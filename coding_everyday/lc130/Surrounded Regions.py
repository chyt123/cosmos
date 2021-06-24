import collections
import math
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visit = [[False for _ in board[0]] for _ in board]
        d = [-1, 0, 1, 0, -1]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n or visit[x][y] or board[x][y] == 'X':
                return
            if board[x][y] == 'O':
                visit[x][y] = True
            for i in range(4):
                newx = x + d[i]
                newy = y + d[i + 1]
                dfs(newx, newy)

        for i in range(n):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[m - 1][i] == 'O':
                dfs(m - 1, i)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][n - 1] == 'O':
                dfs(i, n - 1)

        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == 'O' and not visit[i][j]:
                    board[i][j] = 'X'


if __name__ == "__main__":
    sol = Solution()
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    print(sol.solve(board))
    print(board)


