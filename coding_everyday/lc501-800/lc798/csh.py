import sys


class Solution(object):

    def bestRotation(self, A):
        l = len(A)
        r = list()
        for i in range(0, l):
            if A[i] <= i: # can be move to left
                r.append([0, False])
                r.append([i - A[i], True])

            # every num can be move to right
            move_right_start = i + 1
            move_right_end = min(l - A[i] + i, l-1)
            if move_right_start <= move_right_end:
                r.append([move_right_start, False])
                r.append([move_right_end, True])

        r.sort()
        _max = 0
        p = 0
        K = 0

        for i, e in enumerate(r):
            if not e[1]:
                p += 1
                if p > _max:
                    _max = p
                    K = e[0]
            else:
                p -= 1

        return K


if __name__ == "__main__":
    sol = Solution()
    # A = [2, 3, 1, 4, 0]
    A = [1, 3, 0, 2, 4]
    print sol.bestRotation(A)

