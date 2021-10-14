import collections
import math
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        mem = []

        def backtracking(pos):
            if len(mem) == k:
                ans.append(mem[:])
                return

            for i in range(pos, n + 1):
                mem.append(i)
                backtracking(i + 1)
                mem.pop()

        backtracking(1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 4
    k = 3
    print(sol.combine(n, k))


