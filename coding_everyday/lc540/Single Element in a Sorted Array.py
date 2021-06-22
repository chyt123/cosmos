import collections
import math
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if (m == 0 and nums[m] != nums[m + 1]) or \
                    (m == len(nums) - 1 and nums[m] != nums[m - 1]) or \
                    (nums[m] != nums[m - 1] and nums[m] != nums[m + 1]):
                return nums[m]
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:  # not reach target
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m - 1]:  # not reach target
                    l = m + 1
                else:
                    r = m - 1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3, 7, 7, 10, 11, 11]
    nums = [1]
    print(sol.singleNonDuplicate(nums))


