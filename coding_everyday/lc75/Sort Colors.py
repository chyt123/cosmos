import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def bisort(nums, s, e):
            if s >= e - 1:
                return
            pivot = nums[s]
            l, r = s, e - 1
            while l < r:
                while l < r and nums[r] >= pivot:
                    r -= 1
                nums[l] = nums[r]
                while l < r and nums[l] <= pivot:
                    l += 1
                nums[r] = nums[l]
            nums[l] = pivot
            bisort(nums, s, l)
            bisort(nums, l + 1, e)
        bisort(nums, 0, len(nums))




if __name__ == "__main__":
    sol = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(sol.sortColors(nums))
