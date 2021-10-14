import re
from typing import List
from math import inf


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        rst = [inf for _ in s]
        zeros = [i.start() for i in re.finditer(c, s)]
        for i in zeros:
            rst[i] = 0
        for i in range(1, len(rst)):
            rst[i] = min(rst[i], rst[i-1] + 1)
        for i in range(len(rst) - 2, -1, -1):
            rst[i] = min(rst[i], rst[i+1] + 1)
        return rst


if __name__ == "__main__":
    sol = Solution()
    s = "loveleetcodei"
    c = "e"
    print(sol.shortestToChar(s, c))

        