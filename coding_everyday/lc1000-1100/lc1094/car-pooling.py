class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        n = len(trips)
        i = 0
        off = defaultdict(list)
        for cur in range(1001):
            # print(cur, i, capacity)
            if cur in off:
                while off[cur]:
                    idx = off[cur].pop()
                    capacity += trips[idx][0]
    
            while i < n and cur == trips[i][1]:
                capacity -= trips[i][0]
                off[trips[i][2]].append(i)
                i += 1

            if capacity < 0:
                return False
            if i == n:
                return True
        return True
            

