import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter((s1 + ' ' + s2).split())
        ans = []
        for k, v in c.items():
            if v == 1:
                ans.append(k)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(sol.uncommonFromSentences(s1, s2))
