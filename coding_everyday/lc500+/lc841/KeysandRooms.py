from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visit = [False for _ in rooms]
        self.dps(0, rooms)
        return False not in self.visit

    def dps(self, node, rooms):
        self.visit[node] = True
        for n in rooms[node]:
            if not self.visit[n]:
                self.dps(n, rooms)


if __name__ == "__main__":
    sol = Solution()
    rooms = [[1], [2], [3], []]
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(sol.canVisitAllRooms(rooms))
