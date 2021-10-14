from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def backtracking(level, cur_list, target):
            if target <= 0:
                if target == 0:
                    ans.append(cur_list[:])
                return
            for i in range(level, n):
                cur_list.append(candidates[i])
                backtracking(i, cur_list, target - candidates[i])
                cur_list.pop()

        backtracking(0, [], target)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 5]
    target = 8
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates, target))
