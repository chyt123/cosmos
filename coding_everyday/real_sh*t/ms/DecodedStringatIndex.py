import bisect
import itertools
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


def solution(n):
    ans = []

    for i in range(1, n):
        ans.append(i)
    return ans


if __name__ == "__main__":
    a = 4
    print(solution(a))

# def solution(a, b, c, d):
#     p = set(itertools.permutations([a, b, c, d]))
#     cnt = 0
#     for i in p:
#         x, y, z, w = i
#         hour = 10 * x + y
#         minute = 10 * z + w
#         if 0 <= hour <= 23 and 0 <= minute <= 59:
#             cnt += 1
#     return cnt
#
#
# if __name__ == "__main__":
#     a, b, c, d = 6, 2, 4, 7
#     print(solution(a, b, c, d))