import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        return ' '.join(l[::-1])


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "  Bob    Loves  Alice   ",
        "Alice does not even like bob"
    ]
    for i in test_cases:
        result = sol.reverseWords(i)
        print(result)
