import bisect
import collections
import math
import random
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word: str) -> int:
        ans = sum(i == j for i, j in zip(word, 'acckzz'))
        print(ans)
        return ans


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        if len(wordlist) <= 10:
            for i in wordlist:
                master.guess(i)
            return

        def match(a, b):
            return sum(i == j for i, j in zip(a, b))
        for i in range(10):
            cand = random.choice(wordlist)
            ans = master.guess(cand)
            wordlist = [w for w in wordlist if match(cand, w) == ans]


if __name__ == "__main__":
    sol = Solution()
    master = Master()
    wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    print(sol.findSecretWord(wordlist, master))

