import bisect
import collections
import heapq


class Solution:
    def red_blue_string(self, s, l):
        if l >= len(s):
            return 0
        total = s.count('r')
        maxx = 0
        for i in range(0, len(s) - l + 1):
            num_r = s[i:i + l].count('r')
            maxx = max(maxx, num_r)
        return total - maxx


if __name__ == "__main__":
    sol = Solution()
    s = 'bbbbbbrrrbbbbbbbb'
    l = 5
    print(sol.red_blue_string(s, l))
    a = [(4, (2, 4)), (3, (1, 3))]
    heapq.heapify(a)
    print(a)