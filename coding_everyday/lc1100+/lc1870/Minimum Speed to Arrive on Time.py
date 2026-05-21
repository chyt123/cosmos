from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if math.ceil(hour) < len(dist):
            return -1

        l = 1
        h = math.ceil(max(dist) / 0.01)
        while l < h:
            mid = (l + h) // 2
            time = 0
            for i in range(len(dist) - 1):
                time += math.ceil(dist[i] / mid)
            time += dist[-1] / mid
            # print(l, h, mid, time)
            if time > hour:
                l = mid + 1
            else:
                h = mid

        return l

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1,3,2], 6],
        [[1,3,2], 2.7],
        [[1,3,2], 1.9],
        [[1,1,100000], 2.01],
        [[1,1,100000], 2.12],
    ]
    for i, j in test_cases:
        print(sol.minSpeedOnTime(i, j))
