import collections
import math
from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x:(-len(x), x))
        for word in dictionary:
            pts, ptw = 0, 0
            while pts != len(s) and ptw != len(word):
                if s[pts] == word[ptw]:
                    ptw += 1
                pts += 1
            if ptw == len(word):
                return word
        return ""


if __name__ == "__main__":
    sol = Solution()
    s = "abpcplea"
    dictionary = ["ale", "bapple", "monkey", "plea"]
    print(sol.findLongestWord(s, dictionary))


