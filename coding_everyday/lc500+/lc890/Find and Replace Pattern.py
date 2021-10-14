import collections
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        def find_pattern(s: str) -> str:
            cur = 'a'
            d = dict()
            ans = ''

            for i in s:
                if i not in d:
                    d[i] = cur
                    cur = chr(ord(cur) + 1)
                ans += d[i]
            return ans

        match = find_pattern(pattern)
        return [i for i in words if find_pattern(i) == match]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"],
        [["a", "b", "c"], "a"],
        [["abc", "cba", "xyx", "yxx", "yyx"], "abc"]
    ]
    for i, j in test_cases:
        print(sol.findAndReplacePattern(i, j))


