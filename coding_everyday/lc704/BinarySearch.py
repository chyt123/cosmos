from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    print(sol.search(nums, target))
