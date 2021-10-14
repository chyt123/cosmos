from typing import List
from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(self.calArea(*i) for i in combinations(points, 3))

    @staticmethod
    def calArea(p, q, r):
        return abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]-p[0]*r[1]-q[0]*p[1]-r[0]*q[1])/2


if __name__ == "__main__":
    sol = Solution()
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(sol.largestTriangleArea(points))
