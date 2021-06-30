import bisect
from typing import List
from collections import defaultdict


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[-1])
        mem = [pairs[0]]
        for i in range(1, len(pairs)):
            if pairs[i][0] > mem[-1][1]:
                mem.append(pairs[i])
        return len(mem)


if __name__ == "__main__":
    sol = Solution()
    pairs = [[1,2],[2,8],[1,4],[4,5],[5,6],[6,7]]
    print(sol.findLongestChain(pairs))
