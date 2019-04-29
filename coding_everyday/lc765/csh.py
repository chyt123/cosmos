import collections
class Solution(object):
    def minSwapsCouples(self, row):
        ptr = 0
        cnt = 0
        pos = [0] * len(row)
        for idx, item in enumerate(row):
            pos[item] = idx
        while ptr != len(row) - 2:
            cur = row[ptr]
            nex = row[ptr + 1]

            if cur % 2 == 0:  # even, couple = row[ptr] + 1
                cp = cur + 1
            else:  # odd, couple = row[ptr] - 1
                cp = cur - 1

            print nex, cp
            if nex != cp:
                cp_idx = pos[cp]
                row[ptr + 1], row[cp_idx] = row[cp_idx], row[ptr + 1]
                pos[nex], pos[cp] = pos[cp], pos[nex]
                cnt += 1
            ptr += 2
        return cnt


if __name__ == "__main__":
    sol = Solution()
    row =[10,7,4,2,3,0,9,11,1,5,6,8]
    print sol.minSwapsCouples(row)
