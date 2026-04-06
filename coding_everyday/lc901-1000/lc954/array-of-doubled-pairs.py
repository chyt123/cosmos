class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        pos = []
        neg = []
        d = defaultdict(int)
        for i in arr:
            if i >= 0:
                pos.append(i)
            else:
                neg.append(i)
            d[i] += 1

        pos = sorted(pos)
        neg = sorted(neg, key=lambda x:-x)

        # print(pos, neg, d)
        for i in pos:
            if d[i] > 0:
                if 2*i in d and d[2*i] > 0:
                    d[i] -= 1
                    d[2*i] -= 1
                else:
                    return False

        for i in neg:
            if d[i] > 0:
                if 2*i in d and d[2*i] > 0:
                    d[i] -= 1
                    d[2*i] -= 1
                else:
                    return False
        return True