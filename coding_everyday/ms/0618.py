import bisect
import itertools
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)

# Arrange
# n = 10,
# pre = {
#     1: [2, 3, 4],
#     2: [3, 4],
#     3: [5, 6],
#     4: [],
#     5: [],
#     6: []
# }

# post = {
#     1: [],
#     2: [1],
#     3: [1, 2],
#     4: [1, 2],
#     5: [3]
#     6: [3]
# }

def convert():
    return dict()


def cal_order(pre, post):
    ans = []
    visit = [0 for _ in range(len(pre) + 1)]
    q = deque()
    for k, v in post.items():
        if not v:
            q.append(k)

    while q:
        cur = q.popleft()
        if visit[cur] < 2:
            ans.append(cur)
            visit[cur] += 1
        if visit[cur] == 2:
            return []
        for i in pre[cur]:
            if visit[i] == 0:
                q.append(i)
                visit[i] += 1
        print(q, visit)
    ans.reverse()
    return ans


if __name__ == "__main__":
    pre = {
        1: [2, 3, 4],
        2: [3, 4],
        3: [5, 6],
        4: [],
        5: [],
        6: []
    }
    post = {
        1: [],
        2: [1],
        3: [1, 2],
        4: [1, 2],
        5: [3],
        6: [3]
    }
    # pre_req = dict()
    # post = convert(pre_req)
    print(cal_order(pre, post))


# def solution(n):
#     ans = []
#
#     for i in range(1, n):
#         ans.append(i)
#     return ans
#
#
# if __name__ == "__main__":
#     a = 4
#     print(solution(a))

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