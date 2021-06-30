from typing import List
from collections import deque, OrderedDict
import heapq
from time import time, sleep


def print_func(s):
    print(s, 'Here')


# class RateLimit:
#     def __init__(self, func, limit):
#         self.func = func
#         self.limit = limit / 1000
#         self.timer = 0
#
#     def apply(self):
#         now = time()
#         if self.timer == 0:  # first time
#             self.timer = now
#         elif now - self.timer < self.limit:  # not first time
#             raise RuntimeError('Too many calls within time limitation.')
#         self.func()

# class RateLimit:
#     def __init__(self, func, limit):
#         self.func = func
#         self.q = deque()
#         self.limit = limit
#         self.timer = 0
#
#     def apply(self, *args):
#         now = time()
#         if len(self.q) < self.limit:
#             self.q.append(now)
#         elif now - self.q[0] > 1:
#             self.q.popleft()
#             self.q.append(now)
#         else:
#             raise RuntimeError('Call times beyond limitation in 1 sec.')
#         self.func(args[0])


class RateLimit:
    def __init__(self, func, limit):
        self.func = func
        self.q = deque()
        self.limit = limit
        self.timer = 0

    def apply(self, *args, is_retry=False, retry=3):
        now = time()
        if len(self.q) < self.limit:
            self.q.append(now)
        elif now - self.q[0] > 1:
            self.q.popleft()
            self.q.append(now)
        elif not is_retry:
            for i in range(retry):
                print(f'Retrying...{args}')
                sleep(1)
                if self.apply(*args, True):
                    return True
        elif is_retry:
            return False
        self.func(args[0])
        return True


if __name__ == "__main__":
    # r = RateLimit(print_func, 500)
    # r.apply()
    # r.apply()
    r = RateLimit(print_func, 500)
    for i in range(1010):
        print(r.apply(i))