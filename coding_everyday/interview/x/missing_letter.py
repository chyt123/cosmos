from typing import List
from collections import deque, OrderedDict
import heapq


class Solution:
    def missing_letter(self, sentence: str, dictionary: set) -> list:
        spaces = []
        for idx, i in enumerate(sentence):
            if i == ' ':
                spaces.append(idx)
        ans = []

        def backtracking(s, idx):
            if idx == len(spaces):
                return
            new_s = s[0:spaces[idx]] + 'e' + s[spaces[idx] + 1:]
            backtracking(new_s, idx + 1)
            valid = True
            for i in new_s.split(' '):
                if i not in dictionary:
                    valid = False
                    break
            if valid:
                ans.append(new_s)
            backtracking(s, idx + 1)

        backtracking(sentence, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ['I hav  a bad f  ling about PE', {'I', 'have', 'a', 'bad', 'feeling', 'about', 'PE'}],
        ['I hav  a bad f  ling about PE', {'I', 'have', 'a', 'bad', 'feeling', 'about', 'PE', 'haveea', 'aebad'}],
    ]
    for i, j in test_cases:
        print(sol.missing_letter(i, j))
