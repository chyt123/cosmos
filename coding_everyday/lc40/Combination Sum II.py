import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        num = []
        cand = []
        cnt = collections.Counter(candidates)
        for i in cnt:
            cand.append(i)
            num.append(cnt[i])
        n = len(cand)
        ans = []

        def backtracking(level, cur_list, target):
            if target <= 0:
                if target == 0 and cur_list not in ans:
                    ans.append(cur_list[:])
                return
            for i in range(level, n):
                cur_list.append(cand[i])
                num[i] -= 1
                if num[i] > 0:
                    backtracking(i, cur_list, target - cand[i])
                else:
                    backtracking(i + 1, cur_list, target - cand[i])
                num[i] += 1
                cur_list.pop()

        backtracking(0, [], target)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(sol.combinationSum2(candidates, target))
