from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        l = len(hand)
        if l % W != 0:
            return False
        cnt = Counter(hand)
        sorted_cnt = sorted(cnt)
        print(cnt)
        print(sorted_cnt)
        while len(cnt) >= W:
            print('-------')
            for i in range(W):
                idx = sorted_cnt[i]
                print(i, idx, cnt[idx])
                if i == 0:
                    cur = idx
                else:
                    if idx != cur + 1:
                        return False
                    cur += 1
                cnt[idx] -= 1
            print('    ', cnt)
            print('    ', sorted_cnt)
            while cnt and cnt[sorted_cnt[0]] == 0:
                cnt.pop(sorted_cnt[0])
                sorted_cnt.pop(0)
        if not cnt:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    W = 3
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    W = 3
    # hand = [1, 2, 3, 4, 5]
    # W = 4
    print(sol.isNStraightHand(hand, W))
