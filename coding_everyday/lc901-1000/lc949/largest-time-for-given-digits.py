class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        s = set()
        for p in permutations(arr):
            s.add((str(p[0])+str(p[1]), str(p[2])+str(p[3])))

        l = sorted(list(s), key=lambda x : (-int(x[0]), -int(x[1])))

        for i in l:
            if 0 <= int(i[0]) <= 23 and 0 <= int(i[1]) <= 59:
                return ':'.join(i)
        return ''