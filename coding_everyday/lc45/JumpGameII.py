import math
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [math.inf] * n

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                dp[i] = 0
                continue
            for j in range(1, nums[i] + 1):
                if i + j < n and dp[i + j] + 1 < dp[i]:
                    dp[i] = dp[i + j] + 1
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 1, 1, 4]
    nums = [2, 3, 0, 1, 4]
    nums = [2,1]
    print(sol.jump(nums))
