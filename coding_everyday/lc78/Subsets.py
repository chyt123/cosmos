import collections
import math
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        set_ans = set()

        def backtracking(cur, idx):
            if cur not in set_ans:
                set_ans.add(cur)
            if idx < len(nums):
                backtracking(cur, idx + 1)
                cur += str(nums[idx]) + ','
                backtracking(cur, idx + 1)

        backtracking('', 0)
        ans = []
        for i in set_ans:
            tmp = i.split(',')
            if tmp:
                tmp.pop()
            ans.append([int(i) for i in tmp])

        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3],
        [1],
        [1, -2, 10],
    ]
    for i in test_cases:
        print(sol.subsets(i))


