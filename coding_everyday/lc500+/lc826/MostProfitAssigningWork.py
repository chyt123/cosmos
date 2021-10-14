from math import inf
from typing import List
class Solution:
    # def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    #     rst = 0
    #     worker.sort()
    #     mem = {}
    #     dp = [0 for _ in range(worker[-1] + 1)]
    #     for i, d in enumerate(difficulty):
    #         mem[d] = profit[i] if d not in mem else max(mem[d], profit[i])
    #     for i in range(1, worker[-1] + 1):
    #         dp[i] = dp[i-1]
    #         if i in mem:
    #             dp[i] = max(dp[i], mem[i])
    #     for i in worker:
    #         rst += dp[i] if dp[i] < inf else 0
    #     return rst
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        pro_diff = sorted([(profit[i], difficulty[i]) for i in range(len(worker))], reverse=True)
        worker = sorted(worker, reverse=True)
        rst = 0
        print(pro_diff)
        print(worker)
        for w in worker:
            while pro_diff and w < pro_diff[0][1]:
                pro_diff.pop(0)
            if pro_diff:
                rst += pro_diff[0][0]
        return rst


if __name__ == "__main__":
    sol = Solution()
    difficulty = [68,35,52,47,86]
    profit = [67,17,1,81,3]
    worker = [92,10,85,84,82]
    difficulty = [85,47,57]
    profit = [24,66,99]
    worker = [40,25,25]
    difficulty = [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63]
    profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77]
    worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]
    print(sol.maxProfitAssignment(difficulty, profit, worker))
