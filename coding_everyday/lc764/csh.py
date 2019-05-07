import collections
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        mine_row = [list() for _ in range(N)]
        mine_col = [list() for _ in range(N)]
        for mine in mines:
            mine_row[mine[0]].append(mine[1])
            mine_col[mine[1]].append(mine[0])
        print mine_row
        print mine_col
        mx = 0
        for i in range(N):
            for j in range(N):
                tmp_order = min([
                    i - 0,
                    N - 1 - i,
                    j - 0,
                    N - 1 - j,
                    (min(abs(mine_j - j) for mine_j in mine_row[i]) if mine_row[i] else float('Inf')) - 1,
                    (min(abs(mine_i - i) for mine_i in mine_col[j]) if mine_col[j] else float('Inf')) - 1,
                ]) + 1
                if tmp_order > mx:
                    mx = tmp_order
        return mx


if __name__ == "__main__":
    sol = Solution()
    N = 5
    mines = [[4, 2], [3, 2]]
    print sol.orderOfLargestPlusSign(N, mines)
