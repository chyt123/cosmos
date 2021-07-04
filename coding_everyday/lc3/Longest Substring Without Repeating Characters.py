import collections
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = collections.defaultdict()

        for idx, i in enumerate(nums):
            if target - i in d:
                return [d[target - i], idx]
            d[i] = idx


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[2, 7, 11, 15], 9],
        [[3, 2, 4], 6],
        [[3, 3], 6],
    ]
    for i, j in test_cases:
        print(sol.twoSum(i, j))
