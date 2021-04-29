import bisect
from collections import Counter


class MyCalendarThree:

    def __init__(self):
        self.cal= Counter()

    def book(self, start: int, end: int) -> int:
        self.cal[start] += 1
        self.cal[end] -= 1
        ans = 0
        cur = 0
        for (date, cnt) in sorted(self.cal.items()):
            cur += cnt
            ans = max(ans, cur)
        return ans


if __name__ == "__main__":
    cld = MyCalendarThree()
    date = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    for [start, end] in date:
        print(cld.book(start, end))
