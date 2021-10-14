import collections

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        base = collections.defaultdict(set)
        for i, c in enumerate(bottom):
            base[i].add(c)
        allow = collections.defaultdict(set)
        for w in allowed:
            allow[w[:2]].add(w[2])
        print base, allow

        while len(base) > 1:
            tmp = collections.defaultdict(set)
            for i in xrange(len(base) - 1):
                flag = False
                for w1 in base[i]:
                    for w2 in base[i + 1]:
                        if w1 + w2 in allow.keys():
                            tmp[i] = allow[w1 + w2]
                            flag = True
                if not flag:
                    return False
            base = tmp
        return True


if __name__ == "__main__":
    sol = Solution()
    bottom = "BCD"
    allowed = ["BCF", "BCG", "CDE", "GEA", "FFF"]
    bottom = "AABA"
    allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
    print sol.pyramidTransition(bottom, allowed)
