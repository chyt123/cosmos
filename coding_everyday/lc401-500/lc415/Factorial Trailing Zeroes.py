import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def char2int(ch):
            return ord(ch) - ord('0')

        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            num2 = '0' * (l1 - l2) + num2
        else:
            num1 = '0' * (l2 - l1) + num1

        ans = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        pt = 0
        add = 0
        while pt < max(l1, l2):
            cur_rst = char2int(num1[pt]) + char2int(num2[pt]) + add
            ans += str(cur_rst % 10)
            add = cur_rst // 10
            pt += 1
        if add > 0:
            ans += '1'
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    num1 = "11"
    num2 = "123"
    print(sol.addStrings(num1, num2))
