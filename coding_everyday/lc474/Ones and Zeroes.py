import bisect
from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        weight = []
        for s in strs:
            nz = s.count('0')
            no = len(s) - nz
            weight.append((nz, no))

        mem = defaultdict()

        def helper(wt, idx):
            a, b = wt
            if (wt, idx) in mem:
                return mem[(wt, idx)]
            if idx >= len(strs):
                return 0
            n_zero, n_one = weight[idx]
            new_wt = (a - n_zero, b - n_one)
            if n_zero <= a and n_one <= b:
                mem[(wt, idx)] = max(1 + helper(new_wt, idx + 1), helper(wt, idx + 1))
            else:
                mem[(wt, idx)] = helper(wt, idx + 1)
            return mem[(wt, idx)]
        return helper((m, n), 0)


if __name__ == "__main__":
    sol = Solution()
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(sol.findMaxForm(strs, m, n))
