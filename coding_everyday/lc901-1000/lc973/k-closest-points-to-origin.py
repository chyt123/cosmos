class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_dis = list()
        for x, y in points:
            point_dis.append((x, y, x**2 + y**2))

        point_dis = sorted(point_dis, key=lambda x: x[2])

        ans = []
        for i in range(k):
            x, y, _ = point_dis[i]
            ans.append([x, y])

        return ans