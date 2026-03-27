import bisect
import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # comp = [i for i in range(len(arr))]
        # cnt = 0
        # mem, mem_comp = [], []
        # while arr:
        #     cur = arr.pop()
        #     comp_cur = comp.pop()
        #     bisect.insort_left(mem, cur)
        #     bisect.insort_left(mem_comp, comp_cur)
        #     if mem == mem_comp:
        #         cnt += 1
        #         mem.clear()
        #         mem_comp.clear()
        # return cnt
        maxx = 0
        cnt = 0
        for i in range(len(arr)):
            maxx = max(maxx, arr[i])
            if maxx == i:
                cnt += 1
        return cnt



if __name__ == "__main__":
    sol = Solution()
    arr = [1, 0, 2, 3, 4]
    print(sol.maxChunksToSorted(arr))
