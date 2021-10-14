import collections
import math
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = dict()  # num: [freq, first, last]
        max_freq = 0
        for idx, i in enumerate(nums):
            if i not in d:  # first time
                d[i] = [1, idx, idx]
            else:
                d[i][0] += 1
                d[i][2] = idx
            max_freq = max(max_freq, d[i][0])
        min_dist = math.inf
        for _, v in d.items():
            if v[0] == max_freq:
                min_dist = min(min_dist, v[2] - v[1] + 1)
        return min_dist


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 2, 3, 1, 4, 2],
        [1, 2, 2, 3, 1],
        [1],
    ]
    for i in test_cases:
        print(sol.findShortestSubArray(i))