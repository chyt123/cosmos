import math
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)
        ans = [-1 for _ in nums]
        stack = []
        for idx, i in enumerate(nums):
            if not stack:
                stack.append((i, idx))
                ans[idx] = -1
            else:
                while stack and i > stack[-1][0]:
                    (cur, cur_idx) = stack.pop()
                    ans[cur_idx] = i
                stack.append((i, idx))
        return ans[:n]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 1],
        [1, 2, 3, 4, 3],
        [8, 7, 6, 5, 4, 6, 7],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 2, 1]
    ]
    for i in test_cases:
        print(sol.nextGreaterElements(i))