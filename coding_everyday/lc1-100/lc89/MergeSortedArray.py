from typing import List
from collections import defaultdict


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = ['']
        for _ in range(n):
            ans = [ans[x // 2] + str(x % 2) if x % 4 <= 1 else ans[x // 2] + str((x + 1) % 2) for x in range(len(ans) * 2)]
        return [int(str(x), 2) for x in ans]


if __name__ == "__main__":
    sol = Solution()
    for i in range(1, 5):
        print(sol.grayCode(i))
