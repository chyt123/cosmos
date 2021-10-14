import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = nums[0]
        maax = dp
        for i in range(1, n):
            dp = max(nums[i] + dp, nums[i])
            maax = max(maax, dp)
        return maax


if __name__ == "__main__":
    sol = Solution()
    nums = [5,4,-1,7,8]
    nums = [-1, -2]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(nums))
