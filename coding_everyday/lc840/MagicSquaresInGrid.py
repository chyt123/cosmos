from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        num_row = len(grid)
        num_col = len(grid[0])
        if num_row < 3 or num_col < 3:
            return 0
        cnt = 0
        for i in range(0, num_row - 2):
            for j in range(0, num_col - 2):
                cnt += self.magic(
                    grid[i][j], grid[i][j+1], grid[i][j+2],
                    grid[i+1][j], grid[i+1][j + 1], grid[i+1][j + 2],
                    grid[i+2][j], grid[i+2][j + 1], grid[i+2][j + 2],
                )
        return cnt

    @staticmethod
    def magic(*args):
        if sorted(args) == list(range(1, 10)) and \
                args[0] + args[1] + args[2] == args[3] + args[4] + args[5] == args[6] + args[7] + args[8] == \
                args[0] + args[3] + args[6] == args[1] + args[4] + args[7] == args[2] + args[5] + args[8] == \
                args[0] + args[4] + args[8] == args[2] + args[4] + args[6]:
            return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
    print(sol.numMagicSquaresInside(grid))
