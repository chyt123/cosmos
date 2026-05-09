class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dollars = [0] * n
        for i in range(n):
            cost_1d = dollars[i - 1] + costs[0] if i - 1 >= 0 else costs[0]
            # cost_7d
            j = i
            while j > 0 and not days[i] - days[j - 1] >= 7:
                j -= 1
            cost_7d = dollars[j - 1] + costs[1] if j - 1 >= 0 else costs[1]
            # cost_30d
            j = i
            while j > 0 and not days[i] - days[j - 1] >= 30:
                j -= 1
            cost_30d = dollars[j - 1] + costs[2] if j - 1 >= 0 else costs[2]

            dollars[i] = min(cost_1d, cost_7d, cost_30d)

        return dollars[-1]