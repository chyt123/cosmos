from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mem = []
        minmax = []
        maax = 0
        miin = 10**8 + 1
        for idx, i in enumerate(arr):
            if idx != 0:
                miin, maax = minmax[-1]
            if i >= maax:  # create new group
                maax = i
                mem.append([i])
                minmax.append([i, i])
            elif miin < i < maax:  # to previous group
                mem[-1].append(i)
            else:  # merge
                mem[-1].append(i)
                minmax[-1] = [i, minmax[-1][1]]
                while len(mem) >= 2 and minmax[-1][0] < minmax[-2][1]:
                    pp = mem.pop()
                    mm = minmax.pop()
                    mem[-1].extend(pp)
                    minmax[-1] = [min(mm[0], minmax[-1][0]), max(mm[1], minmax[-1][1])]
            print(f'{mem=}')
            print(f'{minmax=}')
        return len(mem)


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 1, 3, 4, 4]
    arr = [5, 4, 3, 2, 1]
    arr = [2, 1, 3, 0, 4, 4, 5, 3, 5]
    arr = [5,1,1,8,1,6,5,9,7,8]
    arr = [1,1,0,0,1]
    print(sol.maxChunksToSorted(arr))
