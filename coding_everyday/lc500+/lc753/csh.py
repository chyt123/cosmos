import collections

class Solution(object):
    def crackSafe(self, n, k):
        res = "0" * n
        visit = [res]
        for i in xrange(k ** n):
            pre = res[len(res) - n + 1:len(res)]
            print "PRE", pre
            for j in xrange(k - 1, -1, -1):
                cur = pre + str(j)
                if cur not in visit:
                    visit.append(cur)
                    res += str(j)
                    break
        return res


if __name__ == "__main__":
    sol = Solution()
    n = 1
    k = 3
    print sol.crackSafe(n, k)
