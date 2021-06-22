import bisect
import collections
import math
from typing import List


class Solution:
    def frequencySort(self, s: str) -> str:
        ct = collections.Counter(s)
        ct_list = sorted(ct.items(), key=lambda x:-x[1])
        ans = ''
        for ch, num in ct_list:
            ans += ch * num
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = 'tree'
    print(sol.frequencySort(s))


