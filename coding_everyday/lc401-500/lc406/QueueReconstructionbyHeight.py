import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for i in people:
            ans.insert(i[1], i)
        return ans
        # people.sort(key=lambda x: (x[1], x[0]))
        # ans = [people[0]]
        # for idx, i in enumerate(people):
        #     if idx == 0:
        #         continue
        #     cnt = 0
        #     for jdx, j in enumerate(ans):
        #         if i[0] <= j[0]:
        #             cnt += 1
        #         if cnt == i[1] + 1:
        #             ans.insert(jdx, i)
        #             break
        #         elif jdx == len(ans) - 1:
        #             ans.insert(jdx + 1, i)
        #             break
        # return ans

if __name__ == "__main__":
    sol = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    print(sol.reconstructQueue(people))