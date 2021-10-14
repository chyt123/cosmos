from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {i for idx, i in enumerate(fronts) if i == backs[idx]}
        ans = 2001
        for num in fronts + backs:
            if num not in same:
                ans = min(ans, num)
        return ans if ans < 2001 else 0


if __name__ == "__main__":
    sol = Solution()
    fronts = [1,2,4,4,7]
    backs = [1,3,4,1,3]
    print(sol.flipgame(fronts, backs))
