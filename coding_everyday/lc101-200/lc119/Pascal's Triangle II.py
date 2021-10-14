import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        rowIndex += 1
        for i in range(1, rowIndex + 1):
            tmp = []
            for j in range(i):
                if j in [0, i - 1]:
                    tmp.append(1)
                else:
                    tmp.append(ans[-1][j - 1] + ans[-1][j])
            ans.append(tmp)
        return ans[-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        0, 1, 2, 3, 4, 5
    ]
    for i in test_cases:
        result = sol.getRow(i)
        print(result)

