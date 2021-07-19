import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {fruits[0]}
        maxx = 0
        cnt = 1
        for i in range(1, len(fruits)):
            if len(basket) == 1:
                cnt += 1
                basket.add(fruits[i])
            elif fruits[i] in basket:
                cnt += 1
            else:
                maxx = max(maxx, cnt)
                basket = {fruits[pre], fruits[i]}
                cnt = i - pre + 1
            if fruits[i] != fruits[i - 1]:
                pre = i
        maxx = max(maxx, cnt)
        return maxx


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 1],
        [0, 1, 2, 2],
        [1, 2, 3, 2, 2],
        [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4],
        [1, 0, 1, 4, 1, 4, 1, 2, 3]
    ]
    for i in test_cases:
        print(sol.totalFruit(i))

