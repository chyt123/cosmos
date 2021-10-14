import bisect
from typing import List
from collections import defaultdict


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in nums:
            if not dp or i > dp[-1]:
                dp.append(i)
            else:
                idx = bisect.bisect_left(dp, i)
                dp[idx] = i
        return len(dp)


if __name__ == "__main__":
    sol = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(sol.lengthOfLIS(nums))
