class Solution(object):
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = list()
        cnt = 0
        i = 0
        for idx, ch in enumerate(S):
            cnt = cnt + 1 if ch == '1' else cnt - 1
            if cnt == 0:
                ans.append('1' + self.makeLargestSpecial(S[i + 1: idx]) + '0')
                i = idx + 1
        print ans
        return ''.join(sorted(ans, reverse=True))


if __name__ == "__main__":
    sol = Solution()
    S = '11100010'
    print sol.makeLargestSpecial(S)
