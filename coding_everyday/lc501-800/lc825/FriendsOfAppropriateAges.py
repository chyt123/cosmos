from typing import List
from collections import Counter

class Solution:
    # A will not request B if:
        # age[B] <= 0.5 * age[A] + 7
        # age[B] > age[A]
        # age[B] > 100 && age[A] < 100
    def numFriendRequests(self, ages: List[int]) -> int:
        rst = 0
        cnt = Counter(ages)
        sorted_cnt = sorted(cnt)
        print(sorted_cnt)
        print([cnt[i] for i in sorted_cnt])
        for a in range(0, len(sorted_cnt)):
            print(sorted_cnt[a], '------')
            if sorted_cnt[a] > 14:
                rst += cnt[sorted_cnt[a]] * (cnt[sorted_cnt[a]] - 1)
            if a > 0:
                youngest = sorted_cnt[a] * 0.5 + 7
                for b in range(a):
                    if sorted_cnt[b] > youngest:
                        print('--', sorted_cnt[b])
                        rst += cnt[sorted_cnt[a]] * cnt[sorted_cnt[b]]
        return rst


if __name__ == "__main__":
    sol = Solution()
    ages = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
    print(sol.numFriendRequests(ages))
