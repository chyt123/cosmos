import math
class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        cnt = 0
        while K != 1:
            power = math.ceil(math.log(K, 2))
            base = pow(2, power)
            diff = base - K
            K = base / 2 - diff
            cnt += 1

        return cnt % 2


if __name__ == "__main__":
    sol = Solution()
    N = 30
    # K = 434991989
    for K in range(1, 100):
        print sol.kthGrammar(N, K),
    print
