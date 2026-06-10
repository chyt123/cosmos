class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        # change = defaultdict(int)
        # for first, last, seats in bookings:
        #     change[first] += seats
        #     change[last + 1] -= seats
        
        # for i in range(1, n + 1):
        #     delta = change[i] if i in change else 0
        #     ans[i] = ans[i - 1] + delta
        for first, last, seats in bookings:
            ans[first - 1] += seats
            ans[last] -= seats
        
        for i in range(1, n):
            ans[i] += ans[i - 1]
        return ans[:n]
# change = {
#     1: 10
#     2: 20 + 25
#     3: -10
#     4: -20
#     6: -25
# }
# [0 10, 55, 45, 25, 25]
        



        
