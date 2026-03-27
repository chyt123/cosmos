class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt = 0
        for i in S:
            if i in J:
                cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    J = "aA"
    S = "aAAbbbb"
    print sol.numJewelsInStones(J, S)
