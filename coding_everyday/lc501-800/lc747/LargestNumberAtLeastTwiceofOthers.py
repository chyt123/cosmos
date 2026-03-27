from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        m = max(nums)
        n = nums.index(m)
        nums.pop(n)
        sec_m = max(nums)
        if m >= sec_m * 2:
            return n
        else:
            return -1


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 6, 1, 0]
    print(sol.dominantIndex(nums))
