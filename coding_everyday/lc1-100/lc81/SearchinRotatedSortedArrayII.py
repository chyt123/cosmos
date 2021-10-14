from typing import List
from collections import defaultdict


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[m] == nums[l]:
                l += 1
            else:
                if nums[m] <= nums[r - 1]:  # right side in order
                    if nums[m] < target <= nums[r - 1]:
                        l = m + 1
                    else:
                        r = m - 1
                else:  # left side in order
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 2
    nums = [5, 0, 2, 3, 4]
    target = 5
    nums = [3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2]
    target = 10
    nums = [1, 0, 1, 1, 1]
    target = 0
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    target = 13
    print(sol.search(nums, target))
