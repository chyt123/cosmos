import bisect
from typing import List
from collections import defaultdict


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        mem = [1]
        up = None
        for i in range(1, n):
            if nums[i] > nums[i - 1] and up is not False:
                up = False
                mem.append(mem[i - 1] + 1)
            elif nums[i] < nums[i - 1] and up is not True:
                up = True
                mem.append(mem[i - 1] + 1)
            else:
                mem.append(mem[i - 1])
        return mem[-1]


if __name__ == "__main__":
    sol = Solution()
    nums = [20, 1, 1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    nums = [0,2]
    print(sol.wiggleMaxLength(nums))
