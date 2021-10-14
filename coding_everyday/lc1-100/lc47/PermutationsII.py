import copy
import math
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        mem = [{str(nums[0])}]
        print(mem)
        for i in range(1, n):
            tmp = set()
            for j in mem[-1]:
                for k in range(0, len(j) + 1):
                    shadow = j.split(',')
                    shadow.insert(k, str(nums[i]))
                    tmp.add(','.join(shadow))
            mem.append(tmp)
        ans = []
        for i in mem[-1]:
            ans.append([int(x) for x in i.split(',')])
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, -1, 3]
    print(sol.permuteUnique(nums))
