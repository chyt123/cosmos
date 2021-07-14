import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rtn = [[0 for _ in range(n)] for _ in range(n)]
        d = [0, 1, 0, -1, 0]
        x, y = 0, -1
        d_flag = 0
        for i in range(n * n):
            new_x = x + d[d_flag]
            new_y = y + d[d_flag + 1]
            if not (0 <= new_x < n and 0 <= new_y < n and rtn[new_x][new_y] == 0):
                d_flag += 1
                d_flag %= 4
                new_x = x + d[d_flag]
                new_y = y + d[d_flag + 1]
            rtn[new_x][new_y] = i + 1
            x, y = new_x, new_y
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        1, 2, 3, 4, 5
    ]
    for i in test_cases:
        print(sol.generateMatrix(i))
