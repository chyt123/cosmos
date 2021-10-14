import collections
import copy
import math
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            l = [ch for ch in s]
            l.sort()
            d[''.join(l)].append(s)
        ans = []
        for i in d:
            ans.append(d[i])
        return ans


if __name__ == "__main__":
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sol.groupAnagrams(strs))
