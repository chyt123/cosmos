import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        rtn = []
        for i in path:
            if not i:
                continue
            if i == '..':
                if rtn:
                    rtn.pop()
            elif i != '.':
                rtn.append(i)
        rst = ''
        for i in rtn:
            rst += '/' + i
        return rst or '/'


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/",
    ]
    for i in test_cases:
        print(sol.simplifyPath(i))
