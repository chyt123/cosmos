from collections import defaultdict
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        target = summ // 2
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums))]
        for i in range(target + 1):
            dp[0][i] = True if nums[0] == i else False

        for i in range(1, len(nums)):
            for j in range(target + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]] or j == nums[i]
        for i in dp:
            print(i)
        return dp[-1][-1]

        # summ = sum(nums)
        # if summ % 2 != 0:
        #     return False
        # target = summ // 2
        # mem = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        # for i in range(len(mem[0])):
        #     mem[0][i] = False
        # mem[0][0] = True
        #
        # summ = 0
        # for i in range(1, len(nums) + 1):
        #     summ += nums[i - 1]
        #     for j in range(min(summ, target) + 1):
        #         right = False
        #         if j - nums[i - 1] >= 0:
        #             right = mem[i - 1][j - nums[i - 1]]
        #         mem[i][j] = mem[i - 1][j] or right
        # for i in mem:
        #     print(i)
        # return mem[len(nums)][target]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 5, 11, 5]
    nums = [2, 2, 1, 1]
    print(sol.canPartition(nums))
