import collections
import math
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if i < 2:
                dp[i] = max(nums[i], dp[i - 1])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [2]
    print(sol.rob(nums))


