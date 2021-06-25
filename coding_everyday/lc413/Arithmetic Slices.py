import copy
import math
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0 for _ in nums]
        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 7]
    print(sol.numberOfArithmeticSlices(nums))
