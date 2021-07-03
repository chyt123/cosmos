import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            nums[abs(i) - 1] = - abs(nums[abs(i) - 1])
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(sol.findDisappearedNumbers(nums))
