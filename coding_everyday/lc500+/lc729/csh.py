class MyCalendarTwo(object):
    def __init__(self):
        self.booked = list()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i, j in self.booked:
            if start < j and end > i:  # already double booked
                return False

        self.booked.append((start, end))
        return True


if __name__ == "__main__":
    cal = MyCalendarTwo()
    print cal.book(10, 20)
    print cal.book(50, 60)
    print cal.book(10, 40)
    print cal.book(5, 15)
    print cal.book(5, 10)
    print cal.book(25, 55)
