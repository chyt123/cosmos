import bisect
import collections
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnt = collections.Counter(deck)
        cnt = sorted([i[1] for i in cnt.items()])
        if cnt[0] == 1:
            return False
        gcd = cnt[0]
        for i in range(1, len(cnt)):
            gcd = math.gcd(cnt[i], gcd)
            if gcd == 1:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1, 1, 1, 2, 2, 2, 3, 3],
        [1],
        [1, 1],
        [1, 1, 2, 2, 2, 2],
    ]
    for i in test_cases:
        print(sol.hasGroupsSizeX(i))

