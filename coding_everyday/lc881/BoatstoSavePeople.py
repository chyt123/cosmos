import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people.sort()
        pt_h = len(people) - 1
        pt_l = 0
        while pt_h >= pt_l:
            cur = 0
            if cur + people[pt_h] <= limit:
                cur += people[pt_h]
                pt_h -= 1
            if cur + people[pt_l] <= limit:
                cur += people[pt_l]
                pt_l += 1
            cnt += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    people = [3, 2, 3, 2, 2]
    limit = 6
    people = [1, 2]
    limit = 3
    people = [3, 2, 2, 1]
    limit = 3
    print(sol.numRescueBoats(people, limit))
