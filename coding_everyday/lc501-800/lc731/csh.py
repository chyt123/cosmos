import heapq


class MyCalendarTwo(object):
    def __init__(self):
        self.booked = list()
        self.double_booked = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.double_booked:
            if start < j and end > i:  # already double booked
                return False

        for i, j in self.booked:
            if start < j and end > i:  # already booked
                self.double_booked.append((max(start, i), min(end, j)))
        self.booked.append((start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendarTwo()
    cal.book(10, 20)
    cal.book(50, 60)
    cal.book(10, 40)
    cal.book(5, 15)
    cal.book(5, 10)
    cal.book(25, 55)
