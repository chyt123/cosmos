import collections
import math
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        visit = [[False for _ in board[0]] for _ in board]
        self.ans = False

        def backtracking(x, y, lv):
            if visit[x][y] or self.ans:
                return
            if lv + 1 == l:
                if word[lv] == board[x][y]:
                    self.ans = True
                return
            d = [-1, 0, 1, 0, -1]
            visit[x][y] = True
            for i in range(4):
                newx = x + d[i]
                newy = y + d[i + 1]
                if board[x][y] == word[lv] and 0 <= newx < m and 0 <= newy < n and board[newx][newy] == word[lv + 1]:
                    backtracking(newx, newy, lv + 1)
            visit[x][y] = False

        for i in range(m):
            for j in range(n):
                backtracking(i, j, 0)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    board = [["a"]]
    word = "b"
    board = [["b", "b"], ["a", "b"], ["b", "a"]]
    word = "a"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
     ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"]]
    word = "BAAAAAAAAAAAAAA"
    print(sol.exist(board, word))


