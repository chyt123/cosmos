from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = []
        for idx, i in enumerate(temperatures):
            while stack and i > stack[-1][0]:
                pre_num, pre_idx = stack.pop()
                ans[pre_idx] = idx - pre_idx
            stack.append((i, idx))
            ans.append(0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [73, 74, 75, 71, 69, 72, 76, 73],
        [30, 40, 50, 60],
        [30, 60, 90],
    ]
    for i in test_cases:
        print(sol.dailyTemperatures(i))
