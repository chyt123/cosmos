import bisect
import collections


class Solution:
    def oncall(self, oncalls):
        times = []
        people = collections.OrderedDict()
        ans = []
        for i, j, k in oncalls:
            bisect.insort_left(times, j)
            bisect.insort_left(times, k)
            people[i] = [j, k]
        for i in range(1, len(times)):
            start, end = times[i - 1], times[i]
            p_list = []
            for p, t in people.items():
                ps, pe = t[0], t[1]
                if not start >= pe and not end <= ps:
                    p_list.append(p)
            if p_list:
                ans.append([start, end, p_list])
        return ans


if __name__ == "__main__":
    sol = Solution()
    oncalls = [
        ['Abby', 1, 10],
        ['Ben', 5, 7],
        ['Carla', 6, 12],
        ['David', 15, 17],
    ]
    print(sol.oncall(oncalls))