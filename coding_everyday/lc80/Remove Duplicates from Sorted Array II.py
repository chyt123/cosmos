import collections
import math
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = n = len(nums)
        if n <= 2:
            return n
        cur = nums[0]
        first = True
        for i in range(1, n):
            if first and nums[i] == cur:
                first = False
            elif nums[i] == cur:
                nums[i] = math.inf
                k -= 1
            else:
                first = True
                cur = nums[i]
        nums.sort()
        print(nums)
        return k


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 2, 2],
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
    ]
    for i in test_cases:
        print(sol.removeDuplicates(i))


