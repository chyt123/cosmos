import math
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    for i in test_cases:
        print(sol.containsDuplicate(i))