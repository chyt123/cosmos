import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        rob_first = [0 for _ in nums]
        not_rob_first = [0 for _ in nums]
        rob_first[0] = nums[0]
        rob_first[1] = max(nums[0], nums[1])
        not_rob_first[0] = 0
        not_rob_first[1] = nums[1]
        for i in range(2, n):
            rob_first[i] = max(rob_first[i - 2] + nums[i], rob_first[i - 1])
            not_rob_first[i] = max(not_rob_first[i - 2] + nums[i], not_rob_first[i - 1])
        rob_first[-1] = rob_first[-2]
        return max(rob_first[-1], not_rob_first[-1])


if __name__ == "__main__":
    sol = Solution()
    nums = [8, 2, 3, 4, 9]
    print(sol.rob(nums))
