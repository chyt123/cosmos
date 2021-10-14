import bisect
from typing import List
from collections import defaultdict


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        tmp = []

        def bt(lv):
            tmptup = tuple(tmp)
            if tmptup not in ans:
                ans.add(tmptup)
            if lv < len(nums):
                bt(lv + 1)
                idx = bisect.bisect(tmp, nums[lv])
                tmp.insert(idx, nums[lv])
                bt(lv + 1)
                tmp.pop(idx)

        bt(0)
        return [list(x) for x in ans]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 2],
        [0],
    ]
    for i in test_cases:
        print(sol.subsetsWithDup(i))
