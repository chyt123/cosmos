import copy
import math
from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         mem = [[[nums[0]]]]
#         for i in range(1, n):
#             tmp = []
#             for j in mem[-1]:
#                 for k in range(0, len(j) + 1):
#                     shadow = j[:]
#                     shadow.insert(k, nums[i])
#                     tmp.append(shadow)
#             mem.append(tmp)
#         return mem[-1]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtracking(lv):
            if lv == len(nums) - 1:
                ans.append(nums[:])
                return
            for i in range(lv, len(nums)):
                nums[i], nums[lv] = nums[lv], nums[i]
                backtracking(lv + 1)
                nums[i], nums[lv] = nums[lv], nums[i]
        backtracking(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))
