import collections
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        d = set()
        for word in words:
            new_word = ''.join(sorted(word[0::2]) + sorted(word[1::2]))
            if new_word not in d:
                d.add(new_word)
        return len(d)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"],
        ["abc", "acb", "bac", "bca", "cab", "cba"]
    ]
    for i in test_cases:
        print(sol.numSpecialEquivGroups(i))


