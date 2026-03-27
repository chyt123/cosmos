from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        # check board
        row = board[0]
        col = [i[0] for i in board]
        n = len(row)
        if abs(row.count(0) - row.count(1)) > 1 or abs(col.count(0) - col.count(1)) > 1:
            return -1
        r_row = [1 - i for i in row]
        for i in board:
            if i not in [row, r_row]:
                return -1

        # cal moves
        rcnt = 0
        ccnt = 0
        for idx, i in enumerate(row):
            if i != idx % 2:
                rcnt += 1

        for idx, i in enumerate(col):
            if i != idx % 2:
                ccnt += 1

        if n % 2 == 0:
            rcnt = min(rcnt, n - rcnt)
            ccnt = min(ccnt, n - ccnt)
        else:
            rcnt = rcnt if rcnt % 2 == 0 else n - rcnt
            ccnt = ccnt if ccnt % 2 == 0 else n - ccnt
        return (rcnt + ccnt) // 2


if __name__ == "__main__":
    sol = Solution()
    board = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    board = [[0, 1], [1, 0]]
    board = [[1, 0], [1, 0]]
    print(sol.movesToChessboard(board))
