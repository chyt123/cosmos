import bisect
import collections
import heapq
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def move_x(cur_x, tgt_x):
            nonlocal ans
            while cur_x != tgt_x:
                if cur_x < tgt_x:
                    ans += 'D'
                    cur_x += 1
                else:
                    ans += 'U'
                    cur_x -= 1
            return cur_x

        def move_y(cur_y, tgt_y):
            nonlocal ans
            while cur_y != tgt_y:
                if cur_y < tgt_y:
                    ans += 'R'
                    cur_y += 1
                else:
                    ans += 'L'
                    cur_y -= 1
            return cur_y

        d = dict()
        cur = 'a'
        for i in range(6):
            for j in range(5):
                d[cur] = (i, j)
                cur = chr(ord(cur) + 1)
                if i * 5 + j == 25:
                    break
        cur_x, cur_y = 0, 0
        pt = 0
        ans = ''
        while pt < len(target):
            (tgt_x, tgt_y) = d[target[pt]]
            if target[pt] == 'z':
                cur_y = move_y(cur_y, tgt_y)
                cur_x = move_x(cur_x, tgt_x)
            else:
                cur_x = move_x(cur_x, tgt_x)
                cur_y = move_y(cur_y, tgt_y)
            if (cur_x, cur_y) == (tgt_x, tgt_y):
                ans += '!'
            pt += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "leet",
        "code",
        "zdz",
    ]
    for i in test_cases:
        print(sol.alphabetBoardPath(i))

