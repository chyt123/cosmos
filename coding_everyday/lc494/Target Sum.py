import bisect
from typing import List
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = defaultdict()

        def backtracking(idx, t):
            if idx == n:
                if t == 0:
                    return 1
                return 0
            if (idx, t) in mem:
                return mem[idx, t]
            add = backtracking(idx + 1, t - nums[idx])
            sub = backtracking(idx + 1, t + nums[idx])
            mem[(idx, t)] = add + sub
            return mem[(idx, t)]

        ans = backtracking(0, target)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(sol.findTargetSumWays(nums, target))
