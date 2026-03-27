import math
from copy import deepcopy
from typing import List

MOD = 10 ** 9 + 7
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq = [0] * 101
        cnt = [0] * 101
        for i in arr:
            freq[i] += 1

        fix = deepcopy(freq)

        ans = 0
        for i in range(101):
            sum = 0
            if freq[i] > 0:
                sum += i
                freq[i] -= 1
                for j in range(i, 101):
                    if freq[j] > 0:
                        sum += j
                        freq[j] -= 1
                        k = target - sum
                        if sum <= target and j <= k < 101 and freq[k] > 0:
                            if i != j and j != k:
                                ans += fix[i] * fix[j] * fix[k]
                            elif i == j and j != k:
                                ans += math.comb(fix[i], 2) * fix[k]
                            elif i != j and j == k:
                                ans += math.comb(fix[j], 2) * fix[i]
                            elif i == j and j == k:
                                ans += math.comb(fix[i], 3)
                        freq[j] += 1
                        sum -= j
                freq[i] += 1
                sum -= i
        # print(freq)
        return ans % MOD