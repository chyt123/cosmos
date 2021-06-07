from collections import defaultdict
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ = sum(nums)
        if summ % 2 != 0:
            return False
        target = summ // 2
        mem = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for i in range(len(mem[0])):
            mem[0][i] = False
        mem[0][0] = True

        summ = 0
        for i in range(1, len(nums) + 1):
            summ += nums[i - 1]
            for j in range(min(summ, target) + 1):
                right = False
                if j - nums[i - 1] >= 0:
                    right = mem[i - 1][j - nums[i - 1]]
                mem[i][j] = mem[i - 1][j] or right
        for i in mem:
            print(i)
        return mem[len(nums)][target]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 5]
    print(sol.canPartition(nums))
