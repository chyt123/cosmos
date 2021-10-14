import collections
import math
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        longest = 0
        sorted_cnt = sorted(cnt.items())
        if len(sorted_cnt) == 1:
            return 0
        for i in range(1, len(sorted_cnt)):
            if sorted_cnt[i][0] - sorted_cnt[i - 1][0] == 1:
                longest = max(longest, sorted_cnt[i][1] + sorted_cnt[i - 1][1])
        return longest


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 3, 2, 2, 5, 2, 3, 7],
        [1, 2, 3, 4],
        [1, 1, 1, 1],
        [1, 3, 5, 7, 9, 11, 13, 15, 17],
        [-3, -1, -1, -1, -3, -2]
    ]
    for i in test_cases:
        print(sol.findLHS(i))